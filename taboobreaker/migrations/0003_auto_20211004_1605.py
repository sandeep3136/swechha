# Generated by Django 3.1.11 on 2021-10-04 10:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taboobreaker', '0002_questionform_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionform',
            name='ans',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
