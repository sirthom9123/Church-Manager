from django.contrib import admin
from .models import ScheduleMeeting, Minutes



@admin.register(ScheduleMeeting)
class ScheduleMeetingAdmin(admin.ModelAdmin):
    list_display = ('agenda', 'group', 'start_time', 'created')
    list_filter = ('agenda', 'created')
    search_fields = ('title' ,'created')
    
    
admin.site.register(Minutes)