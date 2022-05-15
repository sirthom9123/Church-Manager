from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse


"""Meetings"""
class ScheduleMeeting(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='meeting_group')
    agenda = models.CharField(max_length=200)
    estimated_period = models.CharField(max_length=10)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Scheduled Meetings'


    def __str__(self):
        return f'Scheduled Meeting for {self.agenda}'

    def get_absolute_url(self):
        return reverse("meeting_detail", kwargs={"pk": self.pk})

    @property
    def get_html_url(self):
        url = reverse('meeting_detail', args=(self.pk,))
        return f'<a href="{url}"> {self.agenda} </a>'
    
    
# Minutes Manager
class Minutes(models.Model):
    meeting  = models.ForeignKey(ScheduleMeeting, on_delete=models.CASCADE)
    duration = models.CharField(max_length=10, help_text='how long was the meeting')
    contents = models.TextField(null=True, blank=True)
    recording = models.FileField(null=True, upload_to='minutes/meeting_videos', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Minutes Manager'

    def __str__(self):
        return f'{self.meeting.title} hosted on {self.meeting.start_time} by {self.meeting.user}'

    def get_absolute_url(self):
        return reverse("minutes_detail", kwargs={"pk": self.pk})