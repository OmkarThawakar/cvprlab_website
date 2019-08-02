from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from labsite.models import Member, ResearchScholar


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'password'
        )

class CreateProfileForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.user = User.objects.get(id=user.id)

    class Meta:
        model = Member
        fields = (
            'name',
            'info',
            'type',
            'profile_pic',
            'personal_link',
            'research_topic',
            'linkedin',
            'google_scholar',
            'dblp'
        )

    def save(self, commit=True):

        is_edit = False
        try:
            member = Member.objects.get(user=self.user)
            is_edit = True
        except Member.DoesNotExist:
            member = Member()

        member.name = self.cleaned_data['name']
        member.info = self.cleaned_data['info']
        member.type = self.cleaned_data['type']
        member.profile_pic = self.cleaned_data['profile_pic']
        member.personal_link = self.cleaned_data['personal_link']
        member.research_topic = self.cleaned_data['research_topic']
        member.linkedin = self.cleaned_data['linkedin']
        member.google_scholar = self.cleaned_data['google_scholar']
        member.dblp = self.cleaned_data['dblp']

        if not is_edit:
            member.user = self.user

        member.save()
        return member

class CreateBlogForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(CreateBlogForm, self).__init__(*args, **kwargs)
        self.user = User.objects.get(id=user.id)

    class Meta:
        model = ResearchScholar
        fields = (
            'contact_numbar',
            'address',
            'blog_photo',
            'topic',
            'current_position',
            'b_tech',
            'm_tech',
            'abstract',
            'objectives',
            'video',
            'phd'
        )

    def save(self, commit=True):

        member = Member.objects.get(user=self.user)
        scholars = ResearchScholar.objects.filter(member=member)

        if scholars.count() > 0:
            scholar = scholars[0]
        else:
            scholar = ResearchScholar()
            scholar.member = member


        scholar.contact_numbar = self.cleaned_data['contact_numbar']
        scholar.address = self.cleaned_data['address']
        scholar.blog_photo = self.cleaned_data['blog_photo']
        scholar.topic = self.cleaned_data['topic']
        scholar.current_position = self.cleaned_data['current_position']
        scholar.b_tech = self.cleaned_data['b_tech']
        scholar.m_tech = self.cleaned_data['m_tech']
        scholar.abstract = self.cleaned_data['abstract']
        scholar.objectives = self.cleaned_data['objectives']
        scholar.video = self.cleaned_data['video']
        scholar.phd = self.cleaned_data['phd']

        scholar.save()

        return scholar
