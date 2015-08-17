# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:42:41 2015

@author: juandaserni
"""

from django.conf.urls import patterns, url
from Books import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'))
        