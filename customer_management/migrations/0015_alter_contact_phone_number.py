# Generated by Django 4.2.3 on 2023-08-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0014_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
