from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from base.models import Contact

from .models import Newsletter
from .forms import NewsletterForm


def newsletter_view(request):
    obj_list = Newsletter.objects.all()
    
    form = NewsletterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully!')
            return redirect('events')
        else:
            messages.error(request, form.errors)
            return redirect('events')
    
    context = {'obj': obj_list, 'form': form}
    return render(request, 'base/newsletter/list.html', context)

def unsubscribe(request):
    sub = Contact.objects.get(email=request.GET['email'])
    if sub.id == request.GET['id']:
        sub.delete()
        messages.success(request, 'Your request has been granted and you will no longer receive emails.')
        return redirect('events')
    else:
        messages.error(request, 'Token expired, please try again or contact us!')
        return redirect('events')
    

def send_notification(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk)
        
    newsletter.send(request)
    messages.success(request, 'Message sent!')
    return redirect('events') 