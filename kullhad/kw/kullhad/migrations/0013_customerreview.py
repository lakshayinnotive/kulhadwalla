# Generated by Django 3.2.7 on 2022-09-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kullhad', '0012_alter_maindata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=' ', upload_to='customerReview/images')),
                ('customer_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=5000)),
            ],
        ),
    ]
