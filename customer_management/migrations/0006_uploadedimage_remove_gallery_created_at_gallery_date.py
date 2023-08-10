# Generated by Django 4.2.3 on 2023-08-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0005_servicetransaction_payment_method_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploaded_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='created_at',
        ),
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]