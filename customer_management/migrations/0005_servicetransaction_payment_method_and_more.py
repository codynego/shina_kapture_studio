# Generated by Django 4.2.3 on 2023-08-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0004_gallery_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetransaction',
            name='payment_method',
            field=models.CharField(choices=[('Transfer', 'Transfer'), ('Cash', 'Cash'), ('POS', 'POS')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='category',
            field=models.CharField(blank=True, choices=[('fashion', 'wedding'), ('lifestyle', 'birthday'), ('natural', 'family pics'), ('videos', 'others')], max_length=100, null=True),
        ),
    ]
