# Generated by Django 3.0.6 on 2020-06-23 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_transactions', '0010_auto_20200622_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debittransaction',
            name='type',
            field=models.CharField(choices=[('debit', 'debit'), ('Transfer', 'Transfer')], default='debit', max_length=250),
        ),
    ]
