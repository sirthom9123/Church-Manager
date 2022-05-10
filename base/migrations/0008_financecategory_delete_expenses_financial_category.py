# Generated by Django 4.0.4 on 2022-05-10 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_financial_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Finance Categories',
            },
        ),
        migrations.DeleteModel(
            name='Expenses',
        ),
        migrations.AddField(
            model_name='financial',
            name='category',
            field=models.ForeignKey(help_text='Is it an income or expense?', null=True, on_delete=django.db.models.deletion.CASCADE, to='base.financecategory'),
        ),
    ]
