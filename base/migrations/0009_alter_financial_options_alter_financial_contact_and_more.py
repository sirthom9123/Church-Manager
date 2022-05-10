# Generated by Django 4.0.4 on 2022-05-10 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_financecategory_delete_expenses_financial_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financial',
            options={'ordering': ('-upload_date',), 'verbose_name_plural': 'Finances'},
        ),
        migrations.AlterField(
            model_name='financial',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.contact'),
        ),
        migrations.AlterField(
            model_name='financial',
            name='profile',
            field=models.ForeignKey(blank=True, help_text='What is the amount for?', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category'),
        ),
    ]
