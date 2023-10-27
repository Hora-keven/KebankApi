# Generated by Django 4.2.6 on 2023-10-27 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kebank', '0012_alter_address_city_alter_address_federative_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='juridic_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='juridic_person_address_JuridicPerson', to='Kebank.juridicperson'),
        ),
        migrations.AddField(
            model_name='address',
            name='legal_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legal_person_address_LegalPerson', to='Kebank.legalperson'),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='federative_unit',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='address',
            name='neighborhood',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='address',
            name='pac',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='public_place',
            field=models.CharField(max_length=100),
        ),
    ]
