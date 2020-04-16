from django.contrib import admin
from kvant_projects.apps.kvant_proj.models import Key_words, Kvantum, Kvantorianec, Master, kvant_projects


# Register your models here.

admin.site.register(Key_words, admin.ModelAdmin)
admin.site.register(Kvantorianec, admin.ModelAdmin)
admin.site.register(Kvantum, admin.ModelAdmin)
admin.site.register(kvant_projects, admin.ModelAdmin)
admin.site.register(Master, admin.ModelAdmin)
