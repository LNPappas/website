# Generated by Django 2.2.5 on 2019-10-02 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signform',
            name='company',
            field=models.CharField(default=django.utils.timezone.now, max_length=264),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signform',
            name='last',
            field=models.CharField(max_length=264),
        ),
    ]
