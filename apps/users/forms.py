# -*- coding: utf-8 -*-
__author__ = 'Bowen'
__date__ = '12/02/2018 22:53'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)