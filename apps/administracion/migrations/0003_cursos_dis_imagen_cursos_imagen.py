# Generated by Django 4.1.1 on 2022-09-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_remove_cursos_dis_imagen_remove_cursos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='dis_imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
