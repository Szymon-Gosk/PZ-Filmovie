"""Url patterns for users app"""
from django.urls import path
from django.contrib.auth import views as authViews
from users.views import (
    signup_view,
    password_change_view,
    password_change_done_view,
    edit_profile_view,
    user_settings_view
)

urlpatterns = [
    path('login/', authViews.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('profile/edit', edit_profile_view, name='profile-edit'),
    path('profile/settings', user_settings_view, name='profile-settings'),
    path('change-password/', password_change_view, name='change-password'),
    path('change-password-done/', password_change_done_view, name='change-password-done'),
    path('password-reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
