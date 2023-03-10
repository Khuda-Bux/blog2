# Generated by Django 4.1.3 on 2023-01-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
