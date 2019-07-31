# Generated by Django 2.2.3 on 2019-07-28 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_plano', models.IntegerField()),
                ('plano', models.CharField(max_length=40)),
                ('menor_percent', models.FloatField()),
                ('maior_percent', models.FloatField()),
                ('valor_minimo', models.FloatField()),
            ],
        ),
    ]