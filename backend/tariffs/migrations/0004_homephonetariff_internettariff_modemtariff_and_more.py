# Generated by Django 5.0.6 on 2024-05-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariffs', '0003_alter_tariff_gigabytes_alter_tariff_minutes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomephoneTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default='', null=True)),
                ('minutes', models.IntegerField(blank=True, default='', null=True)),
                ('gigabytes', models.IntegerField(blank=True, default='', null=True)),
                ('bonus', models.CharField(blank=True, default='', max_length=100)),
                ('sms', models.IntegerField(blank=True, default='', null=True)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('head', models.CharField(max_length=100)),
                ('bonustext', models.CharField(blank=True, default='', max_length=1000)),
                ('speed', models.IntegerField(blank=True, default='', null=True)),
                ('tv', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InternetTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default='', null=True)),
                ('minutes', models.IntegerField(blank=True, default='', null=True)),
                ('gigabytes', models.IntegerField(blank=True, default='', null=True)),
                ('bonus', models.CharField(blank=True, default='', max_length=100)),
                ('sms', models.IntegerField(blank=True, default='', null=True)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('head', models.CharField(max_length=100)),
                ('bonustext', models.CharField(blank=True, default='', max_length=1000)),
                ('speed', models.IntegerField(blank=True, default='', null=True)),
                ('tv', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModemTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default='', null=True)),
                ('minutes', models.IntegerField(blank=True, default='', null=True)),
                ('gigabytes', models.IntegerField(blank=True, default='', null=True)),
                ('bonus', models.CharField(blank=True, default='', max_length=100)),
                ('sms', models.IntegerField(blank=True, default='', null=True)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('head', models.CharField(max_length=100)),
                ('bonustext', models.CharField(blank=True, default='', max_length=1000)),
                ('speed', models.IntegerField(blank=True, default='', null=True)),
                ('tv', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmartTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default='', null=True)),
                ('minutes', models.IntegerField(blank=True, default='', null=True)),
                ('gigabytes', models.IntegerField(blank=True, default='', null=True)),
                ('bonus', models.CharField(blank=True, default='', max_length=100)),
                ('sms', models.IntegerField(blank=True, default='', null=True)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('head', models.CharField(max_length=100)),
                ('bonustext', models.CharField(blank=True, default='', max_length=1000)),
                ('speed', models.IntegerField(blank=True, default='', null=True)),
                ('tv', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(blank=True, default='', null=True)),
                ('minutes', models.IntegerField(blank=True, default='', null=True)),
                ('gigabytes', models.IntegerField(blank=True, default='', null=True)),
                ('bonus', models.CharField(blank=True, default='', max_length=100)),
                ('sms', models.IntegerField(blank=True, default='', null=True)),
                ('link', models.CharField(blank=True, default='', max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('head', models.CharField(max_length=100)),
                ('bonustext', models.CharField(blank=True, default='', max_length=1000)),
                ('speed', models.IntegerField(blank=True, default='', null=True)),
                ('tv', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
    ]