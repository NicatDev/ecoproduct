# Generated by Django 4.2.6 on 2023-10-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0004_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hoverimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
