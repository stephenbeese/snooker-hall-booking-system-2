# Generated by Django 5.0.1 on 2024-07-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_openinghours_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='day_of_week',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True),
        ),
    ]
