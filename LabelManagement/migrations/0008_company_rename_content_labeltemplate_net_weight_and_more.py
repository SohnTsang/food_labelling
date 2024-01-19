# Generated by Django 5.0.1 on 2024-01-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabelManagement', '0007_rename_country_importcountry_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='labeltemplate',
            old_name='content',
            new_name='net_weight',
        ),
        migrations.RemoveField(
            model_name='labeltemplate',
            name='company_address',
        ),
        migrations.RemoveField(
            model_name='labeltemplate',
            name='company_name',
        ),
        migrations.AddField(
            model_name='labeltemplate',
            name='companies',
            field=models.ManyToManyField(blank=True, to='LabelManagement.company'),
        ),
    ]
