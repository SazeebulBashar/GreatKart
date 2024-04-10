from django.urls import path
from . import views

app_name ='accounts'
urlpatterns = [
    path('register', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),

    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('forgot-password', views.forgotPassword, name="forgotPassword"),
    path('reset-password-confirm/<uidb64>/<token>/', views.reset_password_confirm, name="resetPasswordConfirm"),
    path('reset-password', views.reset_password, name="resetPassword"),
]
