# Generated by Django 4.0.4 on 2022-05-15 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulemeeting',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meeting_group', to='auth.group'),
        ),
    ]