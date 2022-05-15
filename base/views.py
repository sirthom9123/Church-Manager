from decimal import Decimal
from datetime import datetime as dt
import json
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from plotly.offline import plot
import pandas as pd
import plotly.express as px
from plotly.graph_objs import scatter
from library.models import Dropbox

from .models import Contact, FinanceCategory, Financial, Project
from .forms import FinancialForm, MemberForm
from meetings.models import ScheduleMeeting
from news.models import Newsletter


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    
    
    financials = Financial.objects.filter(entity__in=groups).order_by('-created')[:3]
    projects = Project.objects.filter(group__in=groups).order_by('-created')[:3]
    meetings = ScheduleMeeting.objects.filter(group__in=groups,start_time__gte=dt.now()).order_by('-id')[:3]
    object_list = Dropbox.objects.filter(group__in=groups).order_by('-id')[:3]
    events = Newsletter.objects.filter(group__in=groups).order_by('-created_at')[:3]

    context = {
        'fin': financials,
        'projects': projects,
        'meeting': meetings,
        'object_list': object_list,
        'events': events,
        }
    return render(request, 'base/dashboard.html', context)

"""Income scripts"""
@login_required(login_url='login')
def financial_form(request):
    user_obj = request.user
    groups = [group for group in user_obj.groups.all()]
    entity = Financial.objects.filter(entity__in=groups).first()
    print(groups, "<<<<<<<<<<<<<<<<<<")
    
    if request.method == "POST":
        form = FinancialForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.entity = [group for group in groups]
            instance.created_by = user_obj
            instance.save()
            
            messages.success(request, 'Record created successfully!')
            return redirect('financial_list')
        else:
            messages.error(request, form.errors)
            return redirect('financial_list')
        

""" Finance """
@login_required(login_url='login')
def financials_list(request, category_slug=None):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    
    categories = FinanceCategory.objects.all()
    
    object_list = Financial.objects.filter(entity__in=groups).order_by('-upload_date')
    
    category = None
    if category_slug:
        category = get_object_or_404(FinanceCategory, slug=category_slug)
        object_list = object_list.filter(category=category)
        
    paginator = Paginator(object_list, 25)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    form = FinancialForm()
    
    context = {
        'fin': page_obj,
        'form': form,
        'category': category,
        'categories': categories,
        }
    return render(request, 'base/financials/list.html', context)


def search_financials(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        financials = Financial.objects.filter(
                        contact__id__istartswith=search_str) | Financial.objects.filter(
                        project__title__icontains=search_str) | Financial.objects.filter(
                        category__name__istartswith=search_str)
        data = financials.values()
        return JsonResponse(list(data), safe=False)



"""Income vs Expenses"""
def get_income_expenses_view(request, category_slug=None):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    income_qs = Financial.objects.filter(entity__in=groups).order_by('upload_date')
        
    _data = [{
        # Amount needs to be summed up
        'Amount': x.amount,
        'Month': x.upload_date.strftime("%b"),
        'Entity': x.entity,
        'Category': x.category,
    } for x in income_qs]

    # DataFrame
    dt = pd.DataFrame(_data)
    
    # Create the graph by finance category
    fig = px.line(dt, x='Month', y='Amount', color='Category', markers=True)
    # fig.update_yaxes(autorange='reversed')
    category_plot = plot(fig, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    
    # # Create the graph by finance entity
    # fig_ = px.line(dt, x='Month', y='Amount', color='Entity', markers=True)
    # # fig.update_yaxes(autorange='reversed')
    # entity_plot_ = plot(fig_, output_type='div', include_plotlyjs=False, show_link=False, link_text="")
    
    context = {'plot': category_plot,}
    return render(request, 'base/financials/index.html', context)



@login_required(login_url='login')
def projects_list(request):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    
    projects = Project.objects.filter(group__in=groups).order_by('-created')
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
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    member = Contact.objects.filter(belong_to__in=groups)
    
    
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
    
    

