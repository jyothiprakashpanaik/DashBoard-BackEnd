# Generated by Django 3.2.8 on 2022-01-29 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0003_auto_20220106_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('ug_pg', models.CharField(choices=[('pg', 'PG'), ('ug', 'UG'), ('both', 'BOTH')], default='both', max_length=6)),
                ('can_edit', models.BooleanField(default=False)),
                ('campus', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.campus')),
                ('institute', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.institute')),
            ],
        ),
    ]
