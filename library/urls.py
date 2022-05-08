from django.urls import path

from . import views

urlpatterns = [
    path('', views.document_library, name='library'),
    path('upload_file_form/', views.upload_file_form, name='upload_file_form'),
    path('document/delete/<pk>/', views.delete_file, name='delete_file'),
    
    
    #category views
    path('category/<slug:category_slug>/', views.document_library, name='file_list_by_category'),
]
