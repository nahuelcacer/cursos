# Generated by Django 4.1.1 on 2022-09-09 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='dis_imagen',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='imagen',
        ),
    ]
