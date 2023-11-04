from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('why-hireglobal/', views.about, name='about'),
    path('jobs/<int:pk>/', views.jobsDetail, name='jobsDetail'),

    path('login/', lambda request: redirect('login', permanent=True)),
    path('register/', lambda request: redirect('register', permanent=True)),
    path('dashboard/', lambda request: redirect('dashboard', permanent=True)),

    path('accounts/', include('accounts.urls')),
    path('employee/', include('employee.urls')),
    path('employer/', include('employer.urls')),
    path('settings/', include('settings.urls')),
    path('chaining/', include('smart_selects.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
