from django.urls import path

from . import views

urlpatterns = [
    path('calendar/', views.meeting_list, name='meeting_list'),
    path('meeting_form/', views.meeting_form, name='meeting_form'),
    path('detail/<pk>/', views.meeting_detail, name='meeting_detail'),
    
    # minutes
    path('minutes/detail/<pk>/', views.minutes_detail, name='minutes_detail'),
    path('minutes/form/<pk>/', views.minutes_form, name='minutes_form'),
]
