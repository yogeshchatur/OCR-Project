# Generated by Django 4.2.11 on 2024-04-02 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0005_alter_uploadimage_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
