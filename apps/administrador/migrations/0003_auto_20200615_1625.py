# Generated by Django 3.0.5 on 2020-06-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_empleados_estadoempleado_tipoempleado_viewempleados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='id_empleado',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='rut_emp',
            field=models.CharField(max_length=255),
        ),
    ]
