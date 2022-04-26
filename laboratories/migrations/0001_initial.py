# Generated by Django 4.0.4 on 2022-04-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recovery', models.CharField(max_length=20)),
                ('wPercentage', models.CharField(max_length=20)),
                ('waterLimit', models.CharField(max_length=20)),
                ('wp', models.CharField(max_length=20)),
                ('plasticityIndex', models.CharField(max_length=20)),
                ('usc', models.CharField(max_length=20)),
                ('classificationAashto', models.CharField(max_length=20)),
                ('volumen', models.CharField(max_length=20)),
                ('percentageGravas', models.CharField(max_length=20)),
                ('percentageArenas', models.CharField(max_length=20)),
                ('percentageFinos', models.CharField(max_length=20)),
            ],
        ),
    ]
