# Generated by Django 4.0.4 on 2022-05-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_contact_code_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='code',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
