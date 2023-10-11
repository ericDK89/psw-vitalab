# Generated by Django 4.2.6 on 2023-10-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposExatames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=1)),
                ('preco', models.FloatField()),
                ('disponivel', models.BooleanField(default=True)),
                ('horario_inicial', models.IntegerField()),
                ('horario_final', models.IntegerField()),
            ],
        ),
    ]