# Generated by Django 4.2.3 on 2023-08-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0006_uploadedimage_remove_gallery_created_at_gallery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetransaction',
            name='created_at',
        ),
        migrations.AddField(
            model_name='servicetransaction',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]