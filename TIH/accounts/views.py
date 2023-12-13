from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Like
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer

class RegisterView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors,
                    'message' : 'something went wrong'
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data' :{},
                'message' : 'your account is created'
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status=status.HTTP_400_BAD_REQUEST)


from rest_framework.response import Response
from rest_framework import permissions, status


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

    def logout(request):
        return Response({"message": "Successfully logged out"},
                        status=status.HTTP_200_OK)


# views.py
from rest_framework import generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
# views.py
from .serializers import LikeSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_view(request):
    user = request.user
    content_type = request.data.get('content_type')
    object_id = request.data.get('object_id')

    try:
        like = Like.objects.get(user=user, content_type=content_type, object_id=object_id)
        like.delete()
        message = 'Like removed'
    except Like.DoesNotExist:
        Like.objects.create(user=user, content_type=content_type, object_id=object_id)
        message = 'Like added'

    return Response({'message': message}, status=status.HTTP_200_OK)
# views.py

from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid login credentials'
                }, status=status.HTTP_400_BAD_REQUEST)

            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                return Response({
                    'data': {'access_token': access_token},
                    'message': 'Login successful'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'data': {},
                    'message': 'Invalid login credentials'
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong'
            }, status=status.HTTP_400_BAD_REQUEST)
# views.py


class BlogCreateView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
