# Generated by Django 4.2.5 on 2023-10-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentform', '0005_remove_school_cycle_period_school_cycle_cycle_period_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_cycle',
            name='cycle_period',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='school_cycle',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='school_cycle',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='school_cycle',
            name='year',
            field=models.CharField(max_length=5),
        ),
    ]
