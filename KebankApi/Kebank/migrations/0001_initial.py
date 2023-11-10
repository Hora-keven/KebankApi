# Generated by Django 4.2.6 on 2023-11-10 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.IntegerField(blank=True)),
                ('number', models.IntegerField(blank=True)),
                ('number_verificate', models.IntegerField(blank=True)),
                ('type_account', models.CharField(max_length=20)),
                ('limit', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoanInstallment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.CharField(max_length=10)),
                ('installment_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Pix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('from_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_account', to='Kebank.account')),
                ('to_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_account', to='Kebank.account')),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalPerson',
            fields=[
                ('born_date', models.DateField()),
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('physical_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='legal_person_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movimentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hour', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_movimentation', to='Kebank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_solicitation', models.DateTimeField(auto_now_add=True)),
                ('fees', models.DecimalField(blank=True, decimal_places=1, max_digits=3)),
                ('date_approved', models.DateField(auto_now_add=True)),
                ('requested_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('approved', models.BooleanField(blank=True)),
                ('installment_quantity', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kebank.account')),
            ],
        ),
        migrations.CreateModel(
            name='JuridicPerson',
            fields=[
                ('state_registration', models.CharField(max_length=11)),
                ('open_date', models.DateField()),
                ('cnpj', models.CharField(max_length=14, primary_key=True, serialize=False, unique=True)),
                ('juridic_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='juridic_person_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contribuition', models.DecimalField(decimal_places=2, max_digits=10)),
                ('investment_type', models.CharField(max_length=30)),
                ('rentability', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('date_closure', models.CharField(max_length=10)),
                ('income', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('administration_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=3)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment', to='Kebank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag_card', models.CharField(blank=True, max_length=20)),
                ('number', models.CharField(blank=True, max_length=16, unique=True)),
                ('validity', models.CharField(blank=True, max_length=7)),
                ('cvv', models.IntegerField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kebank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('federative_unit', models.CharField(max_length=2)),
                ('pac', models.CharField(max_length=10)),
                ('public_place', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('juridic_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='juridic_person_address_JuridicPerson', to='Kebank.juridicperson')),
                ('physical_person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='physical_person_address_LegalPerson', to='Kebank.physicalperson')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='juridic_person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='juridic_person_JuridicPerson', to='Kebank.juridicperson'),
        ),
        migrations.AddField(
            model_name='account',
            name='physical_person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='legal_person_LegalPerson', to='Kebank.physicalperson'),
        ),
    ]
