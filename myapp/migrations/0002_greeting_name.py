# Generated by Django 5.1.7 on 2025-03-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='name',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
