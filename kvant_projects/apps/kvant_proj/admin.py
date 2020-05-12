from django.contrib import admin
from kvant_projects.apps.kvant_proj.models import Key_words, Kvantum, Kvantorianec, Master, Kvant_projects


# Register your models here.

class Kvant_projectsAdmin(admin.ModelAdmin):
    filter_horizontal = ['key_words', 'kvantorianec']
    list_filter = ['kvantum', 'master']


admin.site.register(Key_words, admin.ModelAdmin)
admin.site.register(Kvantorianec, admin.ModelAdmin)
admin.site.register(Kvantum, admin.ModelAdmin)
admin.site.register(Kvant_projects, Kvant_projectsAdmin)
admin.site.register(Master, admin.ModelAdmin)
