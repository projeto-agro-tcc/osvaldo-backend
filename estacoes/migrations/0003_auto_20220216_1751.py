# Generated by Django 3.2.8 on 2022-02-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estacoes', '0002_alter_estacao_estacao_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacao',
            name='latitude',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estacao',
            name='longitude',
            field=models.CharField(max_length=50),
        ),
    ]
