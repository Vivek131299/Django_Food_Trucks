# Generated by Django 5.1 on 2024-08-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_foodtruck_days_hours_alter_foodtruck_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtruck',
            name='approved',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='permit',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='foodtruck',
            name='received',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
