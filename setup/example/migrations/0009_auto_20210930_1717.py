# Generated by Django 3.1.4 on 2021-09-30 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0008_graduates_postgraduates_undergraduates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postgraduates',
            name='graduates_ptr',
        ),
        migrations.RemoveField(
            model_name='postgraduates',
            name='under_inst',
        ),
        migrations.RemoveField(
            model_name='undergraduates',
            name='graduates_ptr',
        ),
        migrations.RemoveField(
            model_name='undergraduates',
            name='under_inst',
        ),
        migrations.DeleteModel(
            name='Graduates',
        ),
        migrations.DeleteModel(
            name='PostGraduates',
        ),
        migrations.DeleteModel(
            name='UnderGraduates',
        ),
    ]
