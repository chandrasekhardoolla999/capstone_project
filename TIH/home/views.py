from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from rest_framework.permissions import  IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class BlogView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            data = request.data
            print(request.user)
            serializer = BlogSerializer(data = data)
            return Response
        except Exception as e:
            print(e)
