# Generated by Django 2.1.3 on 2019-01-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_user_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pesel',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
