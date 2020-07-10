# Generated by Django 3.0.5 on 2020-05-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoHabitacion',
            fields=[
                ('id_estado_habitacion', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado_habitacion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estado_habitacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoHabitacion',
            fields=[
                ('id_tipohabitacion', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo_habitacion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tipo_habitacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ViewHabitaciones',
            fields=[
                ('id_habitacion', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_habitacion', models.CharField(max_length=255)),
                ('Precio', models.CharField(max_length=255)),
                ('tamanno_hab', models.CharField(max_length=255)),
                ('banno', models.CharField(max_length=255)),
                ('estado_habitacion', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'view_habitaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.AutoField(primary_key=True, serialize=False)),
                ('tamanno_hab', models.CharField(max_length=100)),
                ('banno_privado', models.CharField(max_length=1)),
                ('precio_hab', models.BigIntegerField()),
                ('id_estado_habitacion', models.BigIntegerField()),
                ('id_tipohabitacion', models.BigIntegerField()),
            ],
            options={
                'db_table': 'habitaciones',
                'managed': True,
            },
        ),
    ]