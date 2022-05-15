from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime as dt
from django.contrib.auth.models import User

from .models import Financial, Project
from users.models import UserActivities

@receiver(post_save, sender=Financial)
def post_save_finance_created_by(sender, instance, created, **kwargs):
    if created:
        UserActivities.objects.create(user=instance.created_by, message='{} created a new {} record, ID: {}'.format(instance.created_by.first_name, instance.category, instance.id))
        
    else:
        UserActivities.objects.create(user=instance.created_by, message='{} updated the record, ID: {}'.format(instance.created_by.first_name, instance.id))
        
        
