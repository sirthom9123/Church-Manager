from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.newsletter_view, name='events'),
    path('send_notification/<pk>/', views.send_notification, name='send_notification'),
    path('delete/', views.unsubscribe, name='delete'),
]
