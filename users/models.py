from django.contrib.auth.models import User
from django.db import models

# Create User Activities
class UserActivities(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'User Activities'

    def __str__(self):
        return str(self.user)
    