# Generated by Django 2.2.3 on 2019-07-29 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0002_plano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='id',
        ),
        migrations.AlterField(
            model_name='plano',
            name='cd_plano',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendedores.Vendedor'),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
    ]
