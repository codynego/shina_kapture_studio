# Generated by Django 4.2.3 on 2023-08-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('images', models.ImageField(upload_to='images/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_management.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('service_type', models.CharField(choices=[('passport', 'passport'), ('photoshoot', 'photoshoot'), ('photo_printing', 'photo_printing')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=20)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_management.customer')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_management.gallery')),
            ],
        ),
    ]
