from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('finances/', views.financials_list, name='financial_list'),
    path('financial_form/', views.financial_form, name='financial_form'),
    path('search-financials', csrf_exempt(views.search_financials), name='search_financials'),
    path('income-expenses/', views.get_income_expenses_view, name='get_income_expenses_view'),
    path('projects/', views.projects_list, name='project_list'),
    path('search-financials', csrf_exempt(views.search_projects), name='search_financials'),
    path('contacts/', views.members_view, name='members_view'),
    path('contacts-form/<str:id>/', views.edit_member, name='edit_contact'),
    
    
    #category views
    path('category/<slug:category_slug>/', views.financials_list, name='expense_list_by_category'),
    path('contacts/category/<slug:category_slug>/', views.members_view, name='contacts_list_by_category'),
]
