# Generated by Django 4.1.5 on 2023-04-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_truck_warehouse_id_upsaccount_ups_account_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package_info',
            old_name='ups_account',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='package_info',
            name='name',
        ),
        migrations.RemoveField(
            model_name='package_info',
            name='warehouse_x',
        ),
        migrations.RemoveField(
            model_name='package_info',
            name='warehouse_y',
        ),
        migrations.AddField(
            model_name='package_info',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package_info',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='package_info',
            name='ship_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upsaccount',
            name='ups_account_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
