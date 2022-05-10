from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="auth/login.html"), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('register/', views.register, name='register'),
    path('users/profile', views.profile, name='profile'),
    path('users/', views.all_users, name='users'),
    path('users/<int:user_id>', views.user_detail, name='user-detail')
]