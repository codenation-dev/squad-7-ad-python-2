# Generated by Django 2.2.3 on 2019-07-29 01:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0003_auto_20190728_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plano',
            old_name='plano',
            new_name='nm_plano',
        ),
        migrations.RenameField(
            model_name='vendedor',
            old_name='nome',
            new_name='nm_vendedor',
        ),
        migrations.RemoveField(
            model_name='plano',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vendedor',
            name='plano_comissao',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='plano',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='vendedores.Plano'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plano',
            name='cd_plano',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
