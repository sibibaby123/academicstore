# Generated by Django 4.2.6 on 2023-11-22 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('image', models.ImageField(unique=True, upload_to='department')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'department',
                'verbose_name_plural': 'departments',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UserExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('dateofbirth', models.DateField()),
                ('gender', models.BooleanField(default=True)),
                ('address', models.TextField(max_length=250)),
                ('phonenumber', models.CharField(max_length=20, unique=True)),
                ('purpose', models.CharField(default='', max_length=20)),
                ('exampaper', models.CharField(default='', max_length=20)),
                ('pen', models.CharField(default='', max_length=20)),
                ('material', models.CharField(default='', max_length=20)),
                ('books', models.CharField(default='', max_length=20)),
                ('newspaper', models.CharField(default='', max_length=20)),
                ('course', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department'),
        ),
    ]