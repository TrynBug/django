# Generated by Django 3.0.7 on 2020-06-25 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('count', models.IntegerField()),
                ('text', models.TextField()),
                ('word1', models.CharField(max_length=1000)),
                ('word2', models.CharField(max_length=1000)),
                ('word3', models.CharField(max_length=1000)),
            ],
        ),
    ]
