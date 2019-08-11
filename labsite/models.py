from django.db import models
import datetime
from django.contrib.auth.models import User

class Publication(models.Model):
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=[('Conf', 'Conference'), ('Journal', 'Journal')])
    publisher = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.now)
    pdf = models.CharField(max_length=1000, blank=True, default='')
    code = models.CharField(max_length=1000, blank=True, default='')
    impact_factor = models.FloatField(max_length=5, blank=True, default='')

    def __str__(self):
        return self.title

class Member(models.Model):
    type_choices = [
                    ('M.Tech', 'M.Tech'),
                    ('B.Tech', 'B.Tech'),
                    ('Intern', 'Intern'),
                    ('Research Scholar', 'Research Scholar')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.fields.CharField(max_length=500)
    type = models.fields.CharField(max_length=100, choices=type_choices)
    profile_pic = models.FileField(upload_to='people', default='')
    personal_link = models.URLField(default='',blank=True)
    research_topic = models.CharField(max_length=200)
    linkedin = models.URLField(default='',blank=True)
    google_scholar = models.URLField(default='',blank=True)
    dblp = models.URLField(default='',blank=True)

    def __str__(self):
        return self.user.username

class ResearchScholar(models.Model):
    type_choices = [('Completed', 'Completed'),
                    ('On Going', 'On Going')]
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    contact_numbar = models.IntegerField(max_length=13)
    address = models.CharField(max_length=200,default='CVPR Lab, IIT Ropar,India')
    blog_photo = models.FileField(upload_to='blog_photo', default='')
    topic = models.CharField(max_length=200, default='Coming Soon!')
    current_position = models.CharField(max_length=200, default='Research Scholar, CVPR Lab, EED')
    b_tech = models.CharField(max_length=200, default='')
    m_tech = models.CharField(max_length=200, default='')
    abstract = models.TextField(max_length=1000)
    objectives = models.CharField(max_length=500, default='')
    video = models.FileField(upload_to='video', default='')
    phd = models.fields.CharField(max_length=100, choices=type_choices)

    def __str__(self):
        return self.member.user.username

class GalleryImage(models.Model):
    caption = models.CharField(max_length=500)
    date = models.DateField(default=datetime.datetime.now)
    image = models.FileField(upload_to='gallery_image',default='')

    def __str__(self):
        return self.caption

class News(models.Model):
    news = models.CharField(max_length=500)
    date = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.news

class Projects(models.Model):
    project_choices = [('Completed', 'Completed'),
                    ('On Going', 'On Going')]
    domain = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField(default=datetime.datetime.now)
    photo = models.FileField(upload_to='gallery_image', default='')
    title = models.CharField(max_length=500)
    status = models.fields.CharField(max_length=100, choices=project_choices, default='')

    def __str__(self):
        return self.title
