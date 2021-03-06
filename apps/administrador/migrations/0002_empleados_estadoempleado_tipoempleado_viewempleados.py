# Generated by Django 3.0.5 on 2020-05-31 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewEmpleados',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_emp', models.CharField(max_length=255)),
                ('tipo_empleado', models.CharField(max_length=255)),
                ('nombres_emp', models.CharField(max_length=255)),
                ('apellidos_emp', models.CharField(max_length=255)),
                ('FECHANAC', models.DateField()),
                ('fono_emp', models.CharField(max_length=255)),
                ('email_emp', models.CharField(max_length=255)),
                ('estado_empleado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'view_empleados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='empleados',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('rut_emp', models.CharField(max_length=255, unique=True)),
                ('nombres_emp', models.CharField(max_length=255)),
                ('apellidos_emp', models.CharField(max_length=255)),
                ('fono_emp', models.CharField(max_length=255)),
                ('email_emp', models.CharField(max_length=255)),
                ('fechanac_emp', models.DateField()),
                ('id_estadoempleado', models.IntegerField()),
                ('id_tipoempleado', models.IntegerField()),
            ],
            options={
                'db_table': 'empleados',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EstadoEmpleado',
            fields=[
                ('id_estadoempleado', models.IntegerField(primary_key=True, serialize=False)),
                ('estado_empleado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'estado_empleado',
                'ordering': ['id_estadoempleado'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoEmpleado',
            fields=[
                ('id_tipoempleado', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_empleado', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tipo_empleado',
                'managed': True,
            },
        ),
    ]
