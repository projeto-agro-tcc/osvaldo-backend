# Generated by Django 3.2.8 on 2021-10-25 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='estacoes', to='empresas.empresa')),
            ],
            options={
                'db_table': 'en_estacoes',
            },
        ),
    ]