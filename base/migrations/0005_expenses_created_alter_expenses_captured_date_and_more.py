# Generated by Django 4.0.4 on 2022-05-06 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_financial_options_alter_financial_upload_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='captured_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
