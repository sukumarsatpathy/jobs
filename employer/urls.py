from django.urls import path
from . import views

urlpatterns = [
    path('companyList/', views.companyList, name='companyList'), # Read
    path('companyCreate/', views.companyCreate, name='companyCreate'),  # Create
    path('companyEdit/<int:pk>', views.companyEdit, name='companyEdit'),  # Update
    path('companyDelete/<int:pk>', views.companyDelete, name='companyDelete'),  # Delete

    path('jobList/', views.jobList, name='jobList'), # Read
    path('jobCreate/', views.jobCreate, name='jobCreate'),  # Create
    path('jobEdit/<int:pk>', views.jobEdit, name='jobEdit'),  # Update
    path('jobDelete/<int:pk>', views.jobDelete, name='jobDelete'),  # Delete
]