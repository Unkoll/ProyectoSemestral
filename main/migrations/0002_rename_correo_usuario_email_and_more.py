# Generated by Django 4.2.2 on 2023-06-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='correo',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombres',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
