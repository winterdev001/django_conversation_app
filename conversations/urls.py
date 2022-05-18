from django.contrib.auth import views as auth_views
from django.urls import path
from conversations.views import users

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="auth/login.html"), name='root'),
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="auth/logout.html"), name='logout'),
    path('register/', users.register, name='register'),
    path('users/profile', users.profile, name='profile'),
    path('users/', users.index, name='users'),
    path('users/<int:user_id>', users.detail, name='user-detail')
]