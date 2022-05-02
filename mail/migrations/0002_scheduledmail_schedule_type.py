# Generated by Django 4.0.3 on 2022-04-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduledmail',
            name='schedule_type',
            field=models.CharField(choices=[('once', 'Once'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='once', max_length=16),
        ),
    ]