import calendar
from datetime import date, timedelta, datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe

from .models import ScheduleMeeting, Minutes
from .utils import Calendar
from .forms import MeetingForm, MinutesForm
from .filters import GeneralFilter

# Calendar View
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


# meeting form
@login_required(login_url='login')
def meeting_form(request):
    user = request.user
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting_form = form.save(commit=False)
            meeting_form.owner = user
            meeting_form.save()

            messages.success(request, 'Meeting created!')
            return redirect('meeting_list')
        else:
            messages.error(request, 'Something went wrong!')
            return redirect('meeting_list')
        
# View Calendar and Create Meeting
@login_required(login_url='login')
def meeting_list(request):

    # Calendar
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    
    user_obj = request.user
    groups = user_obj.groups.all().values_list("id", flat=True)
    
    # Meetings
    meeting = ScheduleMeeting.objects.filter(group__in=groups, start_time__gte=datetime.now()).order_by('-created')
    old_meeting = ScheduleMeeting.objects.filter(start_time__lte=datetime.now()).order_by('-created')
    
    # Filter meetings by agenda
    filters = GeneralFilter(request.GET, queryset=meeting)
    meeting = filters.qs
    filters = GeneralFilter(request.GET, queryset=old_meeting)
    old_meeting = filters.qs
    
    
    form = MeetingForm()
    
    context = {
        'calendar': html_cal,
        'prev_month': prev_month(d),
        'next_month': next_month(d),
        'meeting': meeting,
        'form': form, 
        'old_meeting': old_meeting,
        'filters': filters
        }
    return render(request, 'base/meetings/list.html', context)

# Meeting Detail
@login_required(login_url='login')
def meeting_detail(request, pk):
    
    meeting = get_object_or_404(ScheduleMeeting, pk=pk)

    try:
        minutes = Minutes.objects.get(meeting=meeting)  # minutes
    except: 
        minutes = None
    
    if request.method == 'POST':
        meeting_form = MeetingForm(request.POST, instance=meeting)
        if meeting_form.is_valid():
            meeting_form.save()
            messages.success(request, 'updated meeting details')
            return redirect('meeting_detail', meeting.pk)
        else: 
            messages.error(request, meeting_form.errors)
            return redirect('meeting_detail', meeting.pk)
    else:
        meeting_form = MeetingForm(instance=meeting)
            
    # Minutes form
    minutes_form = MinutesForm(instance=minutes)    

    
    context = {
        'meeting': meeting,         
        'minutes': minutes,
        'meeting_form': meeting_form,
        'form': minutes_form,
        }
    return render(request, 'base/meetings/detail.html', context)


# Minutes form
@login_required(login_url='login')
def minutes_form(request, pk):
    user = request.user
    meeting = get_object_or_404(ScheduleMeeting, pk=pk)

    if request.method == 'POST':
        form = MinutesForm(request.POST, request.FILES)
        if form.is_valid():
            minutes_form = form.save(commit=False)
            minutes_form.meeting = meeting
            minutes_form.save()

            messages.success(request, 'Minutes Created')
            return redirect('meeting_detail', meeting.pk)
        else: 
            messages.error(request, form.errors)
            return redirect('meeting_detail', meeting.pk)

# minutes detail
@login_required(login_url='login')
def minutes_detail(request, pk):
    minutes = get_object_or_404(Minutes, pk=pk)

    context = {'minutes': minutes}
    return render(request, 'base/minutes/detail.html', context)