# Generated by Django 4.1.1 on 2022-09-22 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0003_alter_cabecera_options_remove_cabecera_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagoDeuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abono', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Deuda')),
                ('fecha_ab', models.DateField(auto_now_add=True)),
                ('deuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta_cobrar.cabecera')),
            ],
        ),
    ]
