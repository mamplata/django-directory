# LabExam/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from projectmanager import views as pm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='projectmanager/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', pm_views.register, name='register'),
    path('', include('projectmanager.urls')),
]
