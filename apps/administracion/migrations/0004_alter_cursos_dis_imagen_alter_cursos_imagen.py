# Generated by Django 4.1.1 on 2022-09-14 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0003_cursos_dis_imagen_cursos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='dis_imagen',
            field=models.ImageField(null=True, upload_to='disertantes/'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagen/'),
        ),
    ]
