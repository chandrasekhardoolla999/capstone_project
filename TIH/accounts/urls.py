from django.contrib import admin
from django.urls import path
from .views import RegisterView,LogoutView,PostListCreate,PostRetrieveUpdateDestroy,CommentListCreate,CommentRetrieveUpdateDestroy,like_view,LoginView,BlogCreateView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('posts/', PostListCreate.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view()),
    path('comments/', CommentListCreate.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroy.as_view()),
    path('like/', like_view, name='like-view'),
    path('login/', LoginView.as_view(), name='login-view'),
    path('create-blog/', BlogCreateView.as_view(), name='blog-create'),
]
