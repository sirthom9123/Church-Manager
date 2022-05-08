from decimal import Decimal
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
import uuid, datetime as dt
from .utils import create_ref_code

PROFILE_TYPES = (('Tithe', 'Tithe'), ('Offering', 'Offering'), ('Partnership', 'Partnership'), ('Pastors seed', 'Pastors seed'))

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    

class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Entities'
    
class Contact(models.Model):
    id = models.CharField(primary_key=True, default=None, editable=False, max_length=15)
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
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
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
    
    
class Financial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, help_text='Which entity does it belong to?')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Which project does it belong to?', blank=True, null=True)
    profile = models.ForeignKey(Category, on_delete=models.CASCADE, help_text='What is the amount for?')
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    upload_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.profile}-R{self.amount}'
    
    def save(self, *args, **kwargs):
        if self.upload_date is None:
            self.upload_date = timezone.now()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Income'
        ordering = ('-upload_date',)
        

class Expenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, help_text='Which entity does it belong to')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Which project does it belong to', blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    reason = models.TextField()
    captured_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(null=True, auto_now_add=True)
    updated = models.DateTimeField(null=True, auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Expenses'
        ordering = ('-captured_date',)
        
    def __str__(self):
        return f'{self.entity}-R{self.amount} on {self.captured_date}'
    
