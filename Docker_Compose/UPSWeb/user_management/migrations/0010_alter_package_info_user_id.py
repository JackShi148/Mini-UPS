# Generated by Django 4.1.5 on 2023-04-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0009_alter_package_info_status_alter_truck_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_info',
            name='user_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
