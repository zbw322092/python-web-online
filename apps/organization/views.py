# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers

from .models import CourseOrg, CityDict

# Create your views here.


class OrgView(View):

    def get(self, request):
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        all_cities = CityDict.objects.all()
        data = {
            'allOrgs': serializers.serialize('json', all_orgs),
            'allCities': serializers.serialize('json', all_cities),
            'org_nums': org_nums
        }
        return JsonResponse(data)