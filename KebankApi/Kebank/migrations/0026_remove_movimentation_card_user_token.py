# Generated by Django 4.2.6 on 2023-11-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kebank', '0025_movimentation_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentation',
            name='card',
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]