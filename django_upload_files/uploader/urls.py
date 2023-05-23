from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload_file, name='dbf_upload'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('success/', views.upload_success, name='success'),
    path('accounts/profile/', views.accounts_view, name='accounts'),
    path('accounts/profile/error/', views.error_404_view, name='error_404'),
]