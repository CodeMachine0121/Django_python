from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("hello world")

def year_archive(request,year):
     return HttpResponse(year )
def month_archive(request,year,month):
    return HttpResponse(year + "-" + month)