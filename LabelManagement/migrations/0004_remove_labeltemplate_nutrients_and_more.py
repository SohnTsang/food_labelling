# Generated by Django 5.0.1 on 2024-01-15 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LabelManagement', '0003_alter_nutrient_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labeltemplate',
            name='nutrients',
        ),
        migrations.AddField(
            model_name='labeltemplate',
            name='nutrients',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
