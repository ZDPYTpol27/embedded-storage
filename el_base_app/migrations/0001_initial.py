# Generated by Django 3.2.6 on 2021-08-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.FloatField()),
                ('number_of_pcs', models.IntegerField()),
                ('row', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('shelf', models.IntegerField()),
                ('box', models.IntegerField()),
                ('body_type', models.CharField(max_length=5)),
                ('capacity', models.FloatField()),
                ('unit', models.CharField(max_length=5)),
                ('voltage', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.FloatField()),
                ('number_of_pcs', models.IntegerField()),
                ('row', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('shelf', models.IntegerField()),
                ('box', models.IntegerField()),
                ('body_type', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('microcircuit_type', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.FloatField()),
                ('number_of_pcs', models.IntegerField()),
                ('row', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('shelf', models.IntegerField()),
                ('box', models.IntegerField()),
                ('body_type', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('maximum_voltage', models.IntegerField()),
                ('maximum_current', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resistors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.FloatField()),
                ('number_of_pcs', models.IntegerField()),
                ('row', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('shelf', models.IntegerField()),
                ('box', models.IntegerField()),
                ('body_type', models.CharField(max_length=5)),
                ('resistance', models.FloatField()),
                ('unit', models.CharField(choices=[('om', 'om'), ('kom', 'kom'), ('mom', 'mom')], max_length=5)),
                ('deviation', models.FloatField()),
                ('power_dissipation', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transistor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dimensions', models.FloatField()),
                ('number_of_pcs', models.IntegerField()),
                ('row', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('shelf', models.IntegerField()),
                ('box', models.IntegerField()),
                ('body_type', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('junction_type', models.CharField(max_length=5)),
                ('maximum_voltage', models.IntegerField()),
                ('collector_current', models.IntegerField()),
                ('gain', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
