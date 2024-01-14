# Generated by Django 5.0.1 on 2024-01-13 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LabelManagement', '0001_initial'),
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_type', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('details', models.TextField()),
                ('template_used', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='LabelManagement.labeltemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManagement.userinformation')),
            ],
        ),
    ]
