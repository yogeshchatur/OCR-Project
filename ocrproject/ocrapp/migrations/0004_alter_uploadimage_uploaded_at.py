# Generated by Django 4.2.11 on 2024-04-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocrapp', '0003_alter_uploadimage_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
