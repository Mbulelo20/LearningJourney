# Generated by Django 4.2.1 on 2023-08-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_journey_end_date_alter_journey_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journey',
            name='end_date',
        ),
        migrations.AlterField(
            model_name='journey',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]
