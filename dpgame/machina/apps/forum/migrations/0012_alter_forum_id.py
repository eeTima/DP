# Generated by Django 4.1.5 on 2023-01-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20190627_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
