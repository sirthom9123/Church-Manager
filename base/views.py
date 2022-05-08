from decimal import Decimal
from datetime import datetime as dt
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Contact, Entity, Expenses, Financial, Project
from .forms import ExpensesForm, FinancialForm, MemberForm


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    entity = Entity.objects.all()
    entity_group = entity.values_list("id", flat=True)
    
    financials = Financial.objects.filter(entity__in=entity_group).order_by('-created')[:3]
    
    projects = Project.objects.all().order_by('-created')[:3]

 

    context = {
        'fin': financials,
        'projects': projects
        }
    return render(request, 'base/dashboard.html', context)

"""Income scripts"""
@login_required(login_url='login')
def financial_form(request):
    if request.method == "POST":
        form = FinancialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully!')
            return redirect('financial_list')
        else:
            messages.error(request, form.errors)
            return redirect('financial_list')
        

@login_required(login_url='login')
def financials_list(request):
    """ Income """
    entity = Entity.objects.all()
    entity_group = entity.values_list("id", flat=True)
    
    financials = Financial.objects.all().order_by('-upload_date')
    paginator = Paginator(financials, 25)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    form = FinancialForm()
    
    context = {
        'fin': financials,
        'page_obj': page_obj,
        'form': form,
        }
    return render(request, 'base/financials/income/list.html', context)


def search_financials(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        financials = Financial.objects.filter(
                        contact__id__istartswith=search_str) | Financial.objects.filter(
                        entity__name__istartswith=search_str) | Financial.objects.filter(
                        project__title__icontains=search_str)
        data = financials.values()
        return JsonResponse(list(data), safe=False)


"""Expenses scripts"""
def expenses_form(request):
    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
            init = form.save(commit=False)
            init.owner = request.user
            init.save()
            messages.success(request, 'Record created successfully!')
            return redirect('expense_list')
        else:
            messages.error(request, form.errors)
            return redirect('expense_list')
        
        
@login_required(login_url='login')
def expenses_list(request):
    """ Expenses """
    entity = Entity.objects.all()
    entity_group = entity.values_list("id", flat=True)
    
    
    
    expenses = Expenses.objects.all().order_by('-captured_date')
    


    
    paginator = Paginator(expenses, 25)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    form = ExpensesForm()
    
    context = {
        'expenses': expenses,
        'page_obj': page_obj,
        'form': form,
        }
    return render(request, 'base/financials/expenses/list.html', context)


def search_expenses(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        expnses = Expenses.objects.filter(
                        enity__id__istartswith=search_str) | Expenses.objects.filter(
                        project__name__istartswith=search_str) | Expenses.objects.filter(
                        owner__icontains=search_str)
        data = expnses.values()
        return JsonResponse(list(data), safe=False)


"""Income vs Expenses"""
def get_income_expenses_view(request):
    expense_qs = Expenses.objects.all()
    expenses_data = [{
        'Amount': x.amount,
        'Date': x.captured_date.isocalendar()[2]
    } for x in expense_qs]
    
    context = {}
    return render(request, '', context)

@login_required(login_url='login')
def projects_list(request):
    entity = Entity.objects.all()
    entity_group = entity.values_list("id", flat=True)
    
    projects = Project.objects.all().order_by('-created')
    paginator = Paginator(projects, 25)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    context = {
        'projects': projects,
        'page_obj': page_obj,
        }
    return render(request, 'base/projects/list.html', context)

def search_projects(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        projects = Project.objects.filter(
                        title__istartswith=search_str) | Project.objects.filter(
                        entity__name__istartswith=search_str) 
        data = projects.values()
        return JsonResponse(list(data), safe=False)
    
    
    
"""Members"""
@login_required(login_url='login')
def members_view(request):
    member = Contact.objects.all()
    
    
    form = MemberForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully!')
            return redirect('members_view')
        else:
            messages.error(request, form.errors)
            return redirect('members_view')
        
        
    context = {'user_obj': member, 'form': form}
    return render(request, 'base/contacts/members.html', context)

def edit_member(request, id):
    member = get_object_or_404(Contact, id=id)
    
    edit_form = MemberForm(request.POST, instance=member)
    if request.method == 'POST':
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Record created successfully!')
            return redirect('members_view')
        else:
            messages.error(request, edit_form.errors)
            return redirect('members_view')
    else:
        messages.error(request, 'Something went wrong')
        return redirect('members_list')
    
    

