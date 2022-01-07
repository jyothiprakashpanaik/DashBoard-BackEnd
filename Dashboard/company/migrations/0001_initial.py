# Generated by Django 3.2.8 on 2021-12-10 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name_of_the_company',
                 models.CharField(default='', max_length=50)),
                ('profile_offered', models.CharField(default='',
                                                     max_length=50)),
                ('package', models.DecimalField(decimal_places=2,
                                                max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Gim_BBA_BCOM',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('BBA', models.IntegerField(default=-1)),
                ('BCOM', models.IntegerField(default=-1)),
                ('BBA_Logistics', models.IntegerField(default=-1)),
                ('BBA_Business_Analytics', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Gim_MBA',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('MBA_Finance', models.IntegerField(default=-1)),
                ('MBA_HR', models.IntegerField(default=-1)),
                ('MBA_Marketing', models.IntegerField(default=-1)),
                ('MBA_IB', models.IntegerField(default=-1)),
                ('MBA', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Gis_pg',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('MSc_chemistry_analytics', models.IntegerField(default=-1)),
                ('MSc_chemistry_organic', models.IntegerField(default=-1)),
                ('Computer_Science_MCA_3years',
                 models.IntegerField(default=-1)),
                ('Computer_Science_MCA_2years',
                 models.IntegerField(default=-1)),
                ('Biotechnology_MSc', models.IntegerField(default=-1)),
                ('Microbiology_MSc', models.IntegerField(default=-1)),
                ('Food_Science_Technology_MSc',
                 models.IntegerField(default=-1)),
                ('Math_MSc', models.IntegerField(default=-1)),
                ('Math_MSc_Statistics', models.IntegerField(default=-1)),
                ('BioChemisty_Msc', models.IntegerField(default=-1)),
                ('Enviromental_MSc', models.IntegerField(default=-1)),
                ('Physics_and_Electronics_MSc',
                 models.IntegerField(default=-1)),
                ('Physics_and_Electronics_MPC',
                 models.IntegerField(default=-1)),
                ('Physics_and_Electronics_MPCS',
                 models.IntegerField(default=-1)),
                ('Physics_and_Electronics_MECS',
                 models.IntegerField(default=-1)),
                ('Interg_Biotecchnology_MSc', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Gis_ug',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('BSc_Chemistry_Honors', models.IntegerField(default=-1)),
                ('Computer_Science_BCA', models.IntegerField(default=-1)),
                ('Food_Science_Technology_BSc_Hons',
                 models.IntegerField(default=-1)),
                ('Math_BSc', models.IntegerField(default=-1)),
                ('Enviromental_BEM', models.IntegerField(default=-1)),
                ('BioTechnology_BSc', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Git_pg',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('CST', models.IntegerField(default=-1)),
                ('CFIS', models.IntegerField(default=-1)),
                ('DS', models.IntegerField(default=-1)),
                ('VSLI', models.IntegerField(default=-1)),
                ('PSA', models.IntegerField(default=-1)),
                ('MD', models.IntegerField(default=-1)),
                ('MTA', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Git_ug',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('CSE', models.IntegerField(default=-1)),
                ('IT', models.IntegerField(default=-1)),
                ('ECE', models.IntegerField(default=-1)),
                ('EEE', models.IntegerField(default=-1)),
                ('Mech', models.IntegerField(default=-1)),
                ('Civil', models.IntegerField(default=-1)),
                ('Bio', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('company_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='company.company')),
                ('B_Pharmacy', models.IntegerField(default=-1)),
                ('M_Pharmacy_Pharmaceutical_Analysis',
                 models.IntegerField(default=-1)),
                ('M_Pharmacy_Pharmacology', models.IntegerField(default=-1)),
                ('M_Pharmacy_Quality_Assurance',
                 models.IntegerField(default=-1)),
                ('M_Pharmacy_Pharmaceutical_Chemistry',
                 models.IntegerField(default=-1)),
                ('M_Pharmacy_Pharmaceutics', models.IntegerField(default=-1)),
            ],
            bases=('company.company', ),
        ),
    ]
