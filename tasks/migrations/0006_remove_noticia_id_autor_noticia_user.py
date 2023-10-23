# Generated by Django 4.2.6 on 2023-10-22 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_alter_noticia_id_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='id_autor',
        ),
        migrations.AddField(
            model_name='noticia',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
