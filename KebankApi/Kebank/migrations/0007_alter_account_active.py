# Generated by Django 4.2.6 on 2023-10-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kebank', '0006_alter_account_juridic_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]