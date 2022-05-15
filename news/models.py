from django.db import models
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import Group

from base.models import Contact


class Newsletter(models.Model):
    subject = models.CharField(max_length=150)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='newsletter_group')
    contents = models.TextField()
    attachement = models.FileField(upload_to='newsletters/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")
    
    def send(self, request):
        contents = self.contents
        subscribers = Contact.objects.all()
        for sub in subscribers:
            message = EmailMessage(
                    subject=self.subject,
                    body=strip_tags(contents + (
                        "\nTo unsubscribe simply click on this link: {}?email={}&id={}").format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.id)),
                    from_email=settings.EMAIL_HOST_USER,
                    to=[sub.email], attachments=self.attachement
                    )
            message.send(fail_silently=False)
            
