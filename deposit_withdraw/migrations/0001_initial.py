# Generated by Django 3.0.6 on 2020-07-03 20:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_d', models.CharField(max_length=400, unique=True)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=50)),
                ('type', models.CharField(default='withdraw', max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('account_number', models.CharField(max_length=250, null=True)),
                ('bank', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'successful'), ('failed', 'failed')], default='pending', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_d', models.CharField(max_length=400, unique=True)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=50)),
                ('type', models.CharField(default='bank', max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('destination_account', models.CharField(max_length=250, null=True)),
                ('bank', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'successful'), ('failed', 'failed')], default='pending', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_d', models.CharField(max_length=400, unique=True)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=50)),
                ('type', models.CharField(default='Sell', max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('currency', models.CharField(choices=[('bitcoin', 'bitcoin'), ('etherum', 'etherum'), ('litecoin', 'litecoin'), ('bitcoincash', 'bitcoincash')], default='Bitcoin', max_length=250)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'successful'), ('failed', 'failed')], default='pending', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_d', models.CharField(max_length=400, unique=True)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=50)),
                ('type', models.CharField(default='Deposit', max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('bank', models.CharField(max_length=250, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'successful'), ('failed', 'failed')], default='pending', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_d', models.CharField(max_length=400, unique=True)),
                ('amount', models.DecimalField(decimal_places=8, max_digits=50)),
                ('type', models.CharField(default='Buy', max_length=250)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('currency', models.CharField(choices=[('bitcoin', 'bitcoin'), ('etherum', 'etherum'), ('litecoin', 'litecoin'), ('bitcoincash', 'bitcoincash')], default='Bitcoin', max_length=250)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('complete', 'successful'), ('failed', 'failed')], default='pending', max_length=200)),
                ('method', models.CharField(choices=[('debit card', 'debit card'), ('transfer', 'transfer')], default='debit card', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
