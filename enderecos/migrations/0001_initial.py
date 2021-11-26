# Generated by Django 3.2.8 on 2021-11-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=150)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('uf', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'en_enderecos',
            },
        ),
    ]
