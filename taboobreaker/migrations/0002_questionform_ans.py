# Generated by Django 3.1.11 on 2021-09-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taboobreaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionform',
            name='ans',
            field=models.TextField(blank=True),
        ),
    ]
