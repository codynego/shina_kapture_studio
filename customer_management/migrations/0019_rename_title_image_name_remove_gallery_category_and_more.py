# Generated by Django 4.2.3 on 2023-08-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0018_remove_gallery_age_image_age_image_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='category',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='status',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(blank=True, choices=[('fashion', 'wedding'), ('lifestyle', 'birthday'), ('natural', 'family pics'), ('videos', 'others')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.CharField(choices=[('large-small-height', 'large-small-height'), ('small-height', 'small-height'), ('medium-large-height', 'medium-large-height'), ('medium-small-height', 'medium-small-height'), ('large-height', 'large-height')], editable=False, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
