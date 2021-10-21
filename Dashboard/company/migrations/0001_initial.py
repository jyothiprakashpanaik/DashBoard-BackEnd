# Generated by Django 3.2.8 on 2021-10-21 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='companies_stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies_visited', models.IntegerField(default=0)),
                ('companies_yet_to_visit', models.IntegerField(default=0)),
                ('results_pending', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_company', models.CharField(default='', max_length=50)),
                ('profile_offered', models.CharField(default='', max_length=50)),
                ('package', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Gis',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.company')),
                ('MSc_chemistry_analytics', models.IntegerField(default=0)),
                ('MSc_chemistry_organic', models.IntegerField(default=0)),
                ('BSc_Chemistry_Honors', models.IntegerField(default=0)),
                ('Computer_Science_BCA', models.IntegerField(default=0)),
                ('Computer_Science_MCA_3years', models.IntegerField(default=0)),
                ('Computer_Science_MCA_2years', models.IntegerField(default=0)),
                ('Biotechnology_MSc', models.IntegerField(default=0)),
                ('Microbiology_MSc', models.IntegerField(default=0)),
                ('Food_Science_Technology_MSc', models.IntegerField(default=0)),
                ('Food_Science_Technology_BSc_Hons', models.IntegerField(default=0)),
                ('Math_MSc', models.IntegerField(default=0)),
                ('Math_MSc_Statistics', models.IntegerField(default=0)),
                ('Math_BSc', models.IntegerField(default=0)),
                ('BioChemisty_Msc', models.IntegerField(default=0)),
                ('Enviromental_MSc', models.IntegerField(default=0)),
                ('Enviromental_BEM', models.IntegerField(default=0)),
                ('Physics_and_Electronics_MSc', models.IntegerField(default=0)),
                ('Physics_and_Electronics_MPC', models.IntegerField(default=0)),
                ('Physics_and_Electronics_MPCS', models.IntegerField(default=0)),
                ('Physics_and_Electronics_MECS', models.IntegerField(default=0)),
                ('BioTechnology_BSc', models.IntegerField(default=0)),
                ('Interg_Biotecchnology_MSc', models.IntegerField(default=0)),
            ],
            bases=('company.company',),
        ),
        migrations.CreateModel(
            name='Git',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.company')),
                ('CSE', models.IntegerField(default=0)),
                ('IT', models.IntegerField(default=0)),
                ('ECE', models.IntegerField(default=0)),
                ('EEE', models.IntegerField(default=0)),
                ('Mech', models.IntegerField(default=0)),
                ('Civil', models.IntegerField(default=0)),
                ('Bio', models.IntegerField(default=0)),
            ],
            bases=('company.company',),
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('company_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.company')),
                ('B_Pharmacy', models.IntegerField(default=0)),
                ('M_Pharmacy_Pharmaceutical_Analysis', models.IntegerField(default=0)),
                ('M_Pharmacy_Pharmacology', models.IntegerField(default=0)),
                ('M_Pharmacy_Quality_Assurance', models.IntegerField(default=0)),
                ('M_Pharmacy_Pharmaceutical_Chemistry', models.IntegerField(default=0)),
                ('M_Pharmacy_Pharmaceutics', models.IntegerField(default=0)),
            ],
            bases=('company.company',),
        ),
        migrations.CreateModel(
            name='UnderGraduates',
            fields=[
                ('companies_stats_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.companies_stats')),
                ('under_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.branch')),
            ],
            bases=('company.companies_stats',),
        ),
        migrations.CreateModel(
            name='PostGraduates',
            fields=[
                ('companies_stats_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='company.companies_stats')),
                ('under_branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.branch')),
            ],
            bases=('company.companies_stats',),
        ),
    ]
