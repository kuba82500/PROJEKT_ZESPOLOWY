# Generated by Django 2.1.3 on 2019-01-21 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0019_auto_20190117_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='praktyki',
            name='iloscMiejscMax',
        ),
        migrations.RemoveField(
            model_name='praktyki',
            name='iloscMiejscZajetych',
        ),
    ]
