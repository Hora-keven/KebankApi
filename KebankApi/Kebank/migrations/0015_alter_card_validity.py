# Generated by Django 4.2.6 on 2023-10-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kebank', '0014_card_alter_juridicperson_cnpj_alter_legalperson_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='validity',
            field=models.CharField(max_length=7),
        ),
    ]