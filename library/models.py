from django.db import models
from django.utils.timezone import now
from django.urls import reverse
from django.contrib.auth.models import Group, User


# Document library
class DocumentCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Document Categories'

    def __str__(self):
        return self.name


# Document File Share
class Dropbox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, null=True)
    desc = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.title}'

    class Meta:
        verbose_name_plural = 'Library'
        
        
class ShareFileField(models.Model):
    meeting = models.ForeignKey(Dropbox, on_delete=models.CASCADE, related_name='files_field')
    file_field = models.FileField(upload_to='shared/files', null=True)