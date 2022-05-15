# Generated by Django 4.0.4 on 2022-05-15 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('news', '0002_newsletter_attachement'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newsletter_group', to='auth.group'),
        ),
    ]
