# Generated by Django 5.0.1 on 2024-07-04 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_clubdetails_email_clubdetails_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubdetails',
            name='footer_colour',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='clubdetails',
            name='footer_text_colour',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='clubdetails',
            name='header_colour',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AddField(
            model_name='clubdetails',
            name='header_text_colour',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
    ]
