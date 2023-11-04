from django.urls import path
from . import views

urlpatterns = [
    path('webSettings/', views.webSettingsView, name='webSettings'),
    path('mailServer/', views.mailServerView, name='mailServer'),
    # path('paymentGateway/', views.paymentGatewayView, name='paymentGateway'),
    path('messagingAPI/', views.messagingAPIView, name='messagingAPI'),
]