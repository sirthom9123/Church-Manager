# Generated by Django 4.0.4 on 2022-05-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_financial_options_alter_financial_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financial',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]