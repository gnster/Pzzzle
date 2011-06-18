# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from core.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^upload', upload)
)
