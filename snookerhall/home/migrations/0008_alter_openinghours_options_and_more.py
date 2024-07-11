# Generated by Django 5.0.1 on 2024-07-07 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_openinghours_closed_alter_openinghours_closing_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openinghours',
            options={'verbose_name': 'Opening Time', 'verbose_name_plural': 'Opening Times'},
        ),
        migrations.AlterUniqueTogether(
            name='openinghours',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='openinghours',
            name='club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='opening_times', to='home.clubdetails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='day_of_week',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]