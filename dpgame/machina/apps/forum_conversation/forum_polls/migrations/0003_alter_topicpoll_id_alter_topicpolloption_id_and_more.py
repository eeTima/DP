# Generated by Django 4.1.5 on 2023-01-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_polls', '0002_auto_20151105_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topicpoll',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topicpolloption',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='topicpollvote',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
