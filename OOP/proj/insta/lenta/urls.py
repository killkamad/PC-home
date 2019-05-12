from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.com_list, name='com_list'),
    path('feed/', views.com_list, name='com_list'),
    path('feed/post/<int:pk>/', views.com_detail, name='com_detail'),
    path('feed/post/new/', views.com_new, name='com_new'),
    path('feed/post/<int:pk>/edit/', views.com_edit, name='com_edit'),
    path('feed/post/<pk>/remove/', views.com_remove, name='com_remove'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', views.profile, name='view_profile_with_pk'),
    path('profile/edit/', views.profile, name='edit_profile'),
    path('profile/password/', views.change_password, name='change_password'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),



]

from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns+=router.urls