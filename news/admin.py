from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import Newsletter



# Register your models here.
def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected to all subscribers"


@admin.register(Newsletter)
class NewsletterAdmin(SummernoteModelAdmin):
    actions = [send_newsletter]
    summernote_fields = ('contents',)