# Generated by Django 3.0.6 on 2020-06-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_transactions', '0006_auto_20200621_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='debittransaction',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
