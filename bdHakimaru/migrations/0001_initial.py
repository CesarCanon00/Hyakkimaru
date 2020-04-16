# Generated by Django 3.0.2 on 2020-03-20 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('imagen', models.ImageField(null=True, upload_to='lugares')),
            ],
        ),
        migrations.CreateModel(
            name='Monstruo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='monstruos')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdHakimaru.Lugar')),
            ],
            options={
                'verbose_name_plural': 'Monstruos',
            },
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pelea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdHakimaru.Lugar')),
                ('monstruo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdHakimaru.Monstruo')),
            ],
            options={
                'verbose_name_plural': 'Peleas',
            },
        ),
        migrations.AddField(
            model_name='monstruo',
            name='pieza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdHakimaru.Pieza'),
        ),
    ]
