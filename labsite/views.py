from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from labsite.models import Member, Publication, News, Projects, GalleryImage, ResearchScholar
from labsite.forms import (RegistrationForm, CreateProfileForm, CreateBlogForm)
from django.views.generic import View
from django.db.models import Q
from django.contrib.auth.models import User

from django.http import HttpResponse

def home(request):
    news = News.objects.all().order_by('-date')
    return render(request, template_name='labsite/index.html', context={'news': news})

def publications(request):
    pubs = Publication.objects.all().order_by('-date')
    total_conf = Publication.objects.filter(type='Conf').count()
    total_journal = Publication.objects.filter(type='Journal').count()
    year_wise = {}
    for pub in pubs:
        key = str(pub.date.year)
        if key not in year_wise.keys():
            year_wise[key] = {'Journal':[], 'Conf':[]}
            if pub.type == 'Conf':
                year_wise[key]['Conf'].append({'pub':pub,'num':total_conf})
                total_conf-=1
            else:
                year_wise[key]['Journal'].append({'pub':pub,'num':total_journal})
                total_journal-=1

        else:
            if pub.type == 'Conf':
                year_wise[key]['Conf'].append({'pub':pub,'num':total_conf})
                total_conf-=1
            else:
                year_wise[key]['Journal'].append({'pub':pub,'num':total_journal})
                total_journal-=1
    return render(request, template_name='labsite/publications.html', context={'year_wise': year_wise})

def projects(request):
    completed_projects = Projects.objects.filter(status='Completed').order_by('-date')
    ongoing_projects = Projects.objects.filter(status='On Going').order_by('-date')
    return render(request, template_name='labsite/projects.html', context={'completed_projects': completed_projects,'ongoing_projects':ongoing_projects})

def MyBlog(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    member = Member.objects.get(user=user)
    scholar = ResearchScholar.objects.get(member=member)
    pubs = Publication.objects.all()
    objectives = scholar.objectives.split(',')

    publications = pubs.filter(
        Q(authors__contains=user.first_name + ' ' + user.last_name )
    ).distinct()
    return render(request, template_name='labsite/myblog.html', context={'scholar': scholar , 'publications':publications, 'objectives':objectives})

def peoples(request):
    members = Member.objects.all()
    peoples = {'scholars':[],'mtech':[], 'btech':[], 'interns':[]}
    for person in members:
        if person.type == 'Research Scholar':
            peoples['scholars'].append(person)
        elif person.type == 'M.Tech':
                peoples['mtech'].append(person)
        elif person.type == 'B.Tech':
                peoples['btech'].append(person)
        elif person.type == 'Intern':
                peoples['interns'].append(person)
        else:
            pass
    return render(request, template_name='labsite/members.html', context={'peoples':peoples})

def gallery(request):
    images = GalleryImage.objects.all().order_by('-date')
    return render(request, template_name='labsite/gallery.html', context={'images':images})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/register')
    else:
        form = RegistrationForm()

        args = {'form':form }
        return render(request, 'labsite/forms/reg_form.html', args)

class CreateProfileFormView(View):
    form_class = CreateProfileForm
    template_name = 'labsite/forms/create_profile.html'

    def get(self, request):
        user_form = self.form_class(request.user)
        try:
            _ = Member.objects.get(user=request.user)
            member = True
        except Member.DoesNotExist:
            member = False

        return render(request, self.template_name, {'user_form': user_form, 'is_member': member})

    def post(self, request):
        user_form = self.form_class(request.user, request.POST, request.FILES)
        try:
            _ = Member.objects.get(user=request.user)
            member = True
        except Member.DoesNotExist:
            member = False

        if user_form.is_valid():
            member = user_form.save(commit=(not member))

            if member:
                member.save()

            if member is not None:
                return redirect('/')

        return render(request, self.template_name, {'user_form': user_form})

class CreateBlogFormView(View):
    form_class = CreateBlogForm
    template_name = 'labsite/forms/blog_form.html'

    def get(self, request):
        user_form = self.form_class(request.user)

        members = Member.objects.filter(user=request.user)
        is_member = members.count() > 0

        if not is_member:
            return redirect('create_profile')

        return render(request, self.template_name, {'user_form': user_form})

    def post(self, request):
        user_form = self.form_class(request.user, request.POST, request.FILES)

        members = Member.objects.filter(user=request.user)
        is_member = members.count() > 0
        if not is_member:
            return redirect('create_profile')

        scholars = ResearchScholar.objects.filter(member=members[0])
        is_scholar = scholars.count() > 0

        if user_form.is_valid():
            scholar = user_form.save(commit=(not is_scholar))

            if scholar:
                scholar.save()

            if scholar is not None:
                return redirect('/')
        print('Form Not valid!!!!!!')
        return render(request, self.template_name, {'user_form': user_form})

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



