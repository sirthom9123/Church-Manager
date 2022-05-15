from decimal import Decimal
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User, Group
import uuid, datetime as dt
from .utils import create_ref_code

PROFILE_TYPES = (('Tithe', 'Tithe'), ('Offering', 'Offering'), ('Partnership', 'Partnership'), ('Pastors seed', 'Pastors seed'))

class Category(models.Model):
    """Profiles"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class ContactCategory(models.Model):
    """Contact"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Contact Categories'
    

    
class Contact(models.Model):
    id = models.CharField(primary_key=True, default=None, editable=False, max_length=15)
    belong_to = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='contact_group', null=True)
    category = models.ForeignKey(ContactCategory, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)    
    phone = models.CharField(max_length=25, help_text='Phone number must start with country code, e.g. +27')
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        if self.id is None:
            self.id = self.last_name + create_ref_code()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Contact List'
        
    
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='project_group', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_owner', null=True)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Projects'
        ordering = ('-created',)
    
    def __str__(self):
        return self.title
    
    
# Finance library
class FinanceCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(max_length=100, null=True)

    class Meta:
        verbose_name_plural = 'Finance Categories'

    def __str__(self):
        return self.name
    
    
class Financial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.ForeignKey(Group, on_delete=models.CASCADE, help_text='Which entity does it belong to?', related_name='assigned_group', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Which project does it belong to?', blank=True, null=True)
    profile = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='What is the amount for?', blank=True, null=True)
    category = models.ForeignKey(FinanceCategory, on_delete=models.CASCADE, help_text='Is it an income or expense?', null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    upload_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.profile}-R{self.amount}'
    
    def save(self, *args, **kwargs):
        if self.upload_date is None:
            self.upload_date = timezone.now()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Finances'
        ordering = ('-upload_date',)
        

