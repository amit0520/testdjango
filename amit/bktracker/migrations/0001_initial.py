# Generated by Django 2.2.3 on 2019-07-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BKrecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.IntegerField()),
                ('t2', models.IntegerField()),
                ('t3', models.IntegerField()),
                ('t4', models.IntegerField()),
                ('t5', models.IntegerField()),
                ('t6', models.IntegerField()),
                ('plantID', models.CharField(max_length=10)),
                ('lineID', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('bkTime', models.IntegerField()),
            ],
            options={
                'db_table': 'bk_records',
            },
        ),
    ]
