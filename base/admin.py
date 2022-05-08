from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Financial)
class FinancialAdmin(admin.ModelAdmin):
    list_display = ['id', 'entity', 'project', 'amount', 'contact', 'upload_date']
    list_filter = ['project', 'upload_date']
    search_fields = ['project', 'upload_date', 'contact']
    ordering = ['upload_date', 'project']


@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'entity', 'project', 'amount', 'captured_date', 'created']
    list_filter = ['project', 'captured_date']
    search_fields = ['project', 'captured_date', 'contact']
    ordering = ['captured_date', 'project']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'email']
    list_filter = ['id', 'last_name']
    search_fields = ['id', 'last_name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'entity', 'start_date', 'end_date', 'created', 'updated']
    list_filter = ['title', 'entity', 'start_date', 'end_date',]
    search_fields = ['title', 'entity']
    ordering = ['start_date', 'end_date',]



admin.site.register(Entity)
