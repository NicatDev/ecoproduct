# Generated by Django 4.2.6 on 2023-10-31 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0002_homeabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeIcons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
    ]
