# Generated by Django 4.0.4 on 2022-04-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='membresia',
            fields=[
                ('idmembresia', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('tipomenbresia', models.CharField(choices=[('menbresia1', 'logger'), ('menbresia2', 'users'), ('menbresia3', 'pro')], max_length=40)),
            ],
        ),
    ]
