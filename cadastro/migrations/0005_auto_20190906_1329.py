# Generated by Django 2.2.5 on 2019-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20190906_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastro',
            old_name='laboratorio',
            new_name='associado',
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='hora',
            field=models.TimeField(default='13:29:36'),
        ),
    ]
