# Generated by Django 3.2.7 on 2022-09-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullhad', '0013_customerreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
    ]