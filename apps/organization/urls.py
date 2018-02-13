# -*- coding: utf-8 -*-
__author__ = 'Bowen'
__date__ = '13/02/2018 21:07'

from django.conf.urls import url

from .views import OrgView, AddUserAskView, CSRFGeneratorView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),

    url(r'generate_csrf/$', CSRFGeneratorView.as_view())
]