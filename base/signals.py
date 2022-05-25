from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime as dt
from django.contrib.auth.models import User

from .models import Contact, Financial, Project
from users.models import UserActivities

@receiver(post_save, sender=Financial)
def post_save_finance_created_by(sender, instance, created, **kwargs):
    if created:
        UserActivities.objects.create(user=instance.created_by, message='{} created a new {} record, ID: {}'.format(instance.created_by.first_name, instance.category, instance.id))
        
    else:
        UserActivities.objects.create(user=instance.created_by, message='{} updated the record, ID: {}'.format(instance.created_by.first_name, instance.id))
        
        
@receiver(post_save, sender=Contact)
def post_save_contact_list(sender, instance, created, **kwargs):
    if created:
        if instance.category.name == 'Member':
            instance.code = 'Member_' + str(instance.id)
        if instance.category.name == 'Partner':
            instance.code = 'Partner_' + str(instance.id)
        if instance.category.name == 'OnceOff':
            instance.code = 'OnceOff_' + str(instance.id)
        if instance.category.name == 'Investor':
            instance.code = 'Investor_' + str(instance.id)
        if instance.category.name == 'Pledge':
            instance.code = 'Pledge_' + str(instance.id)
        # Save the instance 
        print(instance.code)
        instance.save()
        