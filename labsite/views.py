from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from labsite.models import Member, Publication, News, Projects, GalleryImage

# Create your views here.

from django.http import HttpResponse

def home(request):
    news = News.objects.all().order_by('-date')
    return render(request, template_name='labsite/index.html', context={'news': news})


def publications(request):
    pubs = Publication.objects.all().order_by('-date')
    year_wise = {}
    for pub in pubs:
        key = str(pub.date.year)
        if key in year_wise.keys():
            year_wise[key].append(pub)

        else:
            year_wise[key] = [pub]

    return render(request, template_name='labsite/publications.html', context={'year_wise': year_wise})


def projects(request):
    projects = Projects.objects.all().order_by('-date')
    return render(request, template_name='labsite/projects.html', context={'projects': projects})

def peoples(request):
    return render(request, template_name='labsite/members.html')

def gallery(request):
    images = GalleryImage.objects.all().order_by('-date')
    for img in images:
        print('img ::: ',img.image.url)
    return render(request, template_name='labsite/gallery.html', context={'images':images})




def login_user(request):

    if request.method == 'GET':
        return render(request,template_name='labsite/forms/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect_by_type(request, user)


def redirect_by_type(request, user):
    try:
        member = Member.objects.get(user=user)
    except Member.DoesNotExist:
        member = None

    if member is None or member.type == 'Supervisor':  # Probably a superuser
        return redirect('supervisor_dashboard')

    return redirect('edit_profile')


def supervisor_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login_user')
    return HttpResponse('Yes i am Supervisor!!')



