from django.contrib import admin
from kvant_projects.apps.kvant_proj.models import Key_words
# Register your models here.

admin.site.register(Key_words, admin.ModelAdmin)