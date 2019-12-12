from django.shortcuts import render
from .models import Company, People
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
# Create your views here.
def index(self):
    pass

def all_company(request):
    return JsonResponse(serialize('python', Company.objects.all()), safe=False)

def all_people(request):
    print(serialize('python', People.objects.all()))
    return JsonResponse(serialize('python', People.objects.all()), safe=False)

def clear(request):
    Company.objects.all().delete()
    People.objects.all().delete()
    return 'Objects are all cleared'