# Generated by Django 4.2.6 on 2023-10-22 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha_publicacion',
            field=models.DateTimeField(),
        ),
    ]
