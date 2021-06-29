from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request,HttpResponse
import requests



def index(request):
    json = requests.get('https://api.covid19india.org/data.json').json()
    cases = json['cases_time_series'][-1]
    statewise = json['statewise']
    return render(request,'covid_app/index.html',{'cases':cases,'statewise':statewise[1:]})
