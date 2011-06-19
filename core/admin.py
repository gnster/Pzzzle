# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import *

class CellAdmin(admin.ModelAdmin):
   list_display = ('x', 'y', 'ip', 'lock_dt')

admin.site.register(Cell, CellAdmin)
admin.site.register(Lock)
