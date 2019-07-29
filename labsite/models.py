from django.db import models
import datetime
from django.contrib.auth.models import User


class Publication(models.Model):
    title = models.CharField(max_length=500)
    authors = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=[('Conf', 'Conference'), ('Journal', 'Journal')])
    publisher = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.now)
    pdf = models.CharField(max_length=1000, null=True)
    code = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title


class Member(models.Model):

    type_choices = [('Supervisor', 'Supervisor'),
                    ('M.Tech', 'M.Tech'),
                    ('B.Tech', 'B.Tech'),
                    ('Intern', 'Intern'),
                    ('Research Scholar', 'Research Scholar')]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.fields.TextField()
    type = models.fields.CharField(max_length=100, choices=type_choices)
    profile_pic = models.ImageField()
    publications = models.ManyToManyField(Publication)


class GalleryImage(models.Model):
    caption = models.CharField(max_length=400)
    date = models.DateField(default=datetime.datetime.now)
    path = models.ImageField()





