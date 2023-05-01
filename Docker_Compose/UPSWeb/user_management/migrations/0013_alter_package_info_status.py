# Generated by Django 4.1.5 on 2023-05-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0012_userevaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_info',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('truck_en_route_to_warehouse', 'truck_en_route_to_warehouse'), ('truck_waiting_for_package', 'truck_waiting_for_package'), ('truck_loading', 'truck_loading'), ('truck_loaded', 'truck_loaded'), ('out_for_delivery', 'out_for_delivery'), ('delivered', 'delivered')], max_length=100),
        ),
    ]