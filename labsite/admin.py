from django.contrib import admin
from labsite.models import Member, Publication, News, Projects, GalleryImage, ResearchScholar
# Register your models here.

admin.site.register(Member)
admin.site.register(Publication)
admin.site.register(GalleryImage)
admin.site.register(News)
admin.site.register(Projects)
admin.site.register(ResearchScholar)


