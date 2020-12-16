from django.contrib import admin
from .models import Category, Question, Reply,HackingTutorials

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(HackingTutorials)