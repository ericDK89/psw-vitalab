# Generated by Django 4.2.6 on 2023-10-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0002_rename_tiposexatames_tiposexames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposexames',
            name='tipo',
            field=models.CharField(choices=[('I', 'Exame de imagem'), ('S', 'Exame de sangue')], max_length=1),
        ),
    ]
