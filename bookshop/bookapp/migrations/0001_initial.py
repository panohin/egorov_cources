# Generated by Django 4.0.2 on 2022-02-19 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('rating', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
