from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('financials/', views.financials_list, name='financial_list'),
    path('financial_form/', views.financial_form, name='financial_form'),
    path('search-financials', csrf_exempt(views.search_financials), name='search_financials'),
    path('expenses/', views.expenses_list, name='expense_list'),
    path('expense_form/', views.expenses_form, name='expense_form'),
    path('search-financials', csrf_exempt(views.search_expenses), name='search_financials'),
    path('projects/', views.projects_list, name='project_list'),
    path('search-financials', csrf_exempt(views.search_projects), name='search_financials'),
    path('contacts/', views.members_view, name='members_view'),
    path('contacts-form/<str:id>/', views.edit_member, name='edit_contact')
]
