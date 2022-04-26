# Generated by Django 4.0.4 on 2022-04-26 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('portant_capacity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='idproyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.home1'),
        ),
        migrations.AddField(
            model_name='dimensionespersonalizadas',
            name='idproyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.home1'),
        ),
        migrations.AddField(
            model_name='dimensionespersonalizadas',
            name='joints',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portant_capacity.servicios'),
        ),
        migrations.AddField(
            model_name='datosiniciales',
            name='idproyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.home1'),
        ),
    ]
