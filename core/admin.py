# -*- coding: utf-8 -*-

from django.contrib import admin
from core.models import *

class CellAdmin(admin.ModelAdmin):
   list_display = ('x', 'y', 'ip', 'lock_dt')

admin.site.register(Cell, CellAdmin)

class LockAdmin(admin.ModelAdmin):
   list_display = ('x', 'y', 'ip', 'lock_dt')
   
admin.site.register(Lock, LockAdmin)
