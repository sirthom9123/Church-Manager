# Generated by Django 4.0.4 on 2022-05-15 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0010_financial_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='entity',
        ),
        migrations.AddField(
            model_name='contact',
            name='belong_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_group', to='auth.group'),
        ),
        migrations.AddField(
            model_name='project',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_group', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='entity',
            field=models.ForeignKey(help_text='Which entity does it belong to?', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_group', to='auth.group'),
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
    ]
