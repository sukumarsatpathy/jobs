from django.urls import path
from . import views

urlpatterns = [
    path('empCVList/', views.empCVList, name='empCVList'), # Read
    path('empCVCreate/', views.empCVCreate, name='empCVCreate'),  # Create
    path('empCVEdit/<int:pk>', views.empCVEdit, name='empCVEdit'),  # Update
    path('empCVDelete/<int:pk>', views.empCVDelete, name='empCVDelete'),  # Delete
]