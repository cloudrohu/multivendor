# Generated by Django 4.2 on 2023-10-07 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '5. Category',
            },
        ),
        migrations.CreateModel(
            name='Main_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': '4. Main_category',
            },
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '3. Banner'},
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('name', models.CharField(max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name_plural': '6. Sub_Category',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_category'),
        ),
    ]