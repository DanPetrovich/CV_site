from django.contrib import admin
from .models import *


class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'lastname')


admin.site.register(CVInfo, CVAdmin)
