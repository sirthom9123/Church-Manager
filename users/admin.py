from django.contrib import admin

from .models import UserActivities
from base.utils import CachingPaginator

@admin.register(UserActivities)
class UserActivitiesAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    list_filter = ('user', 'created')
    search_fields = ('user',)

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = UserActivities
