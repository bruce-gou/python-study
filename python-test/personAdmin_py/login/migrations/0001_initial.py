# Generated by Django 2.1.5 on 2019-01-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=10)),
                ('role', models.IntegerField()),
                ('roleName', models.CharField(max_length=10)),
                ('isEnable', models.IntegerField()),
                ('tel', models.CharField(max_length=15, null=True)),
                ('mailbox', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
