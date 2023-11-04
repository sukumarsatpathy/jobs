from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),

    # User Management
    path('userList/', views.userList, name='userList'), # Read
    path('userAdd/', views.userAdd, name='userAdd'), # Create
    path('userEdit/<int:pk>', views.userEdit, name='userEdit'), # Update
    path('userDelete/<int:pk>', views.userDelete, name='userDelete'), # Delete

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
]