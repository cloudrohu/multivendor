# Generated by Django 4.2 on 2023-10-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('Sale', models.IntegerField()),
                ('Quote', models.CharField(max_length=250, null=True)),
                ('Discount_deal', models.CharField(choices=[('Hot Deals', 'Hot Deals'), ('New Arraivels', 'New Arraivels')], max_length=100)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Slider',
            },
        ),
    ]
