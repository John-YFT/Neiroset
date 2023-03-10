from django.contrib import admin
from .models import Bb

class BbAdmin (admin.ModelAdmin):
    list_display = ( 'image', 'rubric', 'published')

admin.site.register(Bb,BbAdmin)
