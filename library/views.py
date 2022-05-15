from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


@login_required(login_url='login')
def document_library(request, category_slug=None):
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    
    categories = DocumentCategory.objects.all()
    form = ShareFileForm()
    file_form = FileFieldForm()
    
    object_list = Dropbox.objects.filter(group__in=groups).order_by('-id') 
    
    category = None
    if category_slug:
        category = get_object_or_404(DocumentCategory, slug=category_slug)
        object_list = object_list.filter(category=category)
            
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page)
    
    context = {
        'page_obj': page_obj,
        'form': form,
        'file_form': file_form,
        'category': category,
        'categories': categories,
    }
    return render(request, 'base/library/index.html', context)


@require_POST
def upload_file_form(request):
    # Form for modal
    form = ShareFileForm(request.POST)
    file_form = FileFieldForm(request.POST, request.FILES)
    files = request.FILES.getlist('file_field')
    if form.is_valid:
        upload_form = form.save(commit=False)
        upload_form.user = request.user
        upload_form.save()

        for f in files:
            upload_file = ShareFileField(file_field=f, meeting=upload_form)
            upload_file.save()

        messages.success(request, 'Document Uploaded!')
        return redirect('library')
    else:
        messages.error(request, form.errors)
        return redirect('library')  
    
    

@login_required(login_url='login')
def delete_file(request, pk):
    user = request.user
    media = get_object_or_404(Dropbox, pk=pk, user=user)

    media.delete()
    messages.error(request, 'Your file has been deleted successfully.')
    return redirect('library')