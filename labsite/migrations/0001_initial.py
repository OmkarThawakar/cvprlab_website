# Generated by Django 2.2.3 on 2019-07-31 08:15

import datetime
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
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('authors', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Conf', 'Conference'), ('Journal', 'Journal')], max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('pdf', models.CharField(blank=True, default='', max_length=1000)),
                ('code', models.CharField(blank=True, default='', max_length=1000)),
                ('impact_factor', models.FloatField(blank=True, default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('type', models.CharField(choices=[('Supervisor', 'Supervisor'), ('M.Tech', 'M.Tech'), ('B.Tech', 'B.Tech'), ('Intern', 'Intern'), ('Research Scholar', 'Research Scholar')], max_length=100)),
                ('profile_pic', models.ImageField(upload_to='')),
                ('publications', models.ManyToManyField(to='labsite.Publication')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
