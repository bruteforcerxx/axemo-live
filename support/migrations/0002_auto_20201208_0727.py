# Generated by Django 3.0.6 on 2020-12-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='full_name',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='i_d',
            field=models.CharField(default='71d72df65e', max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='message',
            field=models.TextField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='email',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='full_name',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='i_d',
            field=models.CharField(default='59b630a3b1', max_length=200),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='inquiry',
            field=models.TextField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='i_d',
            field=models.CharField(default='028aecf902', max_length=200),
        ),
    ]
