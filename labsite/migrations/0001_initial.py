# Generated by Django 2.2.3 on 2019-08-02 10:20

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
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('image', models.FileField(default='', upload_to='gallery_image')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Supervisor', 'Supervisor'), ('M.Tech', 'M.Tech'), ('B.Tech', 'B.Tech'), ('Intern', 'Intern'), ('Research Scholar', 'Research Scholar')], max_length=100)),
                ('profile_pic', models.FileField(default='', upload_to='people')),
                ('personal_link', models.URLField(default='')),
                ('research_topic', models.CharField(max_length=200)),
                ('linkedin', models.URLField(default='')),
                ('google_scholar', models.URLField(default='')),
                ('dblp', models.URLField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.CharField(max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('photo', models.FileField(default='', upload_to='gallery_image')),
                ('title', models.CharField(max_length=500)),
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
            name='ResearchScholar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_numbar', models.IntegerField(max_length=13)),
                ('address', models.CharField(default='CVPR Lab, IIT Ropar,India', max_length=200)),
                ('blog_photo', models.FileField(default='', upload_to='blog_photo')),
                ('topic', models.CharField(default='Coming Soon!', max_length=200)),
                ('current_position', models.CharField(default='Research Scholar, CVPR Lab, EED', max_length=200)),
                ('b_tech', models.CharField(default='', max_length=200)),
                ('m_tech', models.CharField(default='', max_length=200)),
                ('abstract', models.TextField(max_length=1000)),
                ('objectives', models.CharField(default='', max_length=500)),
                ('video', models.FileField(default='', upload_to='video')),
                ('phd', models.CharField(choices=[('Completed', 'Completed'), ('On Going', 'On Going')], max_length=100)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='labsite.Member')),
            ],
        ),
    ]
