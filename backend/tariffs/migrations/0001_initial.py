# Generated by Django 5.0.6 on 2024-05-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('gigabytes', models.IntegerField()),
                ('bonus', models.CharField(max_length=100)),
                ('sms', models.IntegerField()),
                ('link', models.CharField(max_length=100)),
                ('operator', models.CharField(max_length=100)),
                ('bonustext', models.CharField(max_length=1000)),
                ('speed', models.IntegerField()),
                ('tv', models.IntegerField()),
            ],
        ),
    ]