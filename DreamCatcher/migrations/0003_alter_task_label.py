# Generated by Django 4.2.1 on 2023-06-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DreamCatcher', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.CharField(choices=[('Urgent', 'urgent'), ('Important', 'important')], max_length=50),
        ),
    ]
