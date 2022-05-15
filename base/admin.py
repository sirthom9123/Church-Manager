from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ContactCategory)
class ContactCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FinanceCategory)
class FinanceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name',]
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(Financial)
class FinancialAdmin(ImportExportModelAdmin):
    list_display = ['id', 'entity', 'category', 'project', 'amount', 'contact', 'upload_date']
    list_filter = ['category', 'entity', 'project', 'upload_date']
    search_fields = ['project', 'entity', 'category', 'upload_date', 'contact']
    ordering = ['upload_date', 'entity', 'project']
    list_editable = ['category', 'entity']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'belong_to', 'category', 'first_name', 'last_name', 'phone', 'email']
    list_filter = ['id', 'belong_to', 'last_name']
    search_fields = ['id', 'belong_to', 'last_name']
    list_editable = ['belong_to',]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'start_date', 'end_date', 'created', 'updated']
    list_filter = ['title', 'group', 'start_date', 'end_date',]
    search_fields = ['title', 'group']
    ordering = ['group','start_date', 'end_date',]
    list_editable = ['group',]
