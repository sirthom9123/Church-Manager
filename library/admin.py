from django.contrib import admin

from .models import DocumentCategory, ShareFileField, Dropbox


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ShareFileFieldInLine(admin.TabularInline):
    model = ShareFileField


@admin.register(Dropbox)
class ShareFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created')
    list_filter = ('category', 'created')
    search_fields = ('category', 'created')
    inlines = [ShareFileFieldInLine]


