# Generated by Django 3.1.1 on 2021-02-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esuits', '0024_auto_20210205_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answermodel',
            name='answer',
            field=models.TextField(blank=True, default='', verbose_name='回答'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='answer',
            field=models.TextField(blank=True, default='', verbose_name='回答'),
        ),
    ]