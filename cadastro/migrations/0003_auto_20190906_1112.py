# Generated by Django 2.2.5 on 2019-09-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20190906_1020'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='hora',
            field=models.TimeField(default='11:12:32'),
        ),
    ]
