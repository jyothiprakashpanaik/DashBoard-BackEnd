# Generated by Django 3.1.4 on 2021-09-30 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('example', '0004_auto_20210930_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus_name', models.CharField(max_length=30)),
                ('institute_cnt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Institue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=30)),
                ('under_campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.campus')),
            ],
        ),
    ]
