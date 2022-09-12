# Generated by Django 4.1.1 on 2022-09-12 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0003_cursos_dis_imagen_cursos_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('dni', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.cursos')),
            ],
        ),
    ]
