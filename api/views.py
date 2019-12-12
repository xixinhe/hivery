from django.shortcuts import render
from .models import Company, People
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
def index(self):
    pass

def all_company(request):
    return JsonResponse(serialize('python', Company.objects.all()), safe=False)

def employee(request):
    company_id = request.GET.get('company_id', '')
    print(type(company_id))
    employee_list = People.objects.filter(company_id = company_id)
    return JsonResponse(serialize('python', employee_list), safe=False)

def all_people(request):
    people_index_list = request.GET.getlist('people', '')
    people_a=People.objects.get(pk=people_index_list[0])
    people_b=People.objects.get(pk=people_index_list[1])
    friend_list_a = json.loads(people_a.friend)
    friend_list_b = json.loads(people_b.friend)
    common_friends = [ a for a in friend_list_a if a in friend_list_b]
    print(People.objects.filter(pk__in = common_friends, eyeColor = 'brown', has_died = False))
    return JsonResponse(serialize('python', People.objects.all()), safe=False)

def clear(request):
    Company.objects.all().delete()
    People.objects.all().delete()
    return 'Objects are all cleared'