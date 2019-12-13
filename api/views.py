from django.shortcuts import render
from .models import Company, People
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
def index(self):
    pass

def all_employee(request):
    company_id_parameter = request.GET.get('company_id', '')
    company_id = 0
    try:
        company_id = int(company_id_parameter)
    except ValueError:
        error = {'status': 'Failed', 'message': 'company_id has to be integer'}
        return JsonResponse(error, safe=False, status=400)
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        error = {'status': 'Failed', 'message': f'company with this id {company_id} does not exist'}
        return JsonResponse(error, safe=False, status=400)
    employee_list = People.objects.filter(company_id = company_id)
    return JsonResponse(serialize('python', employee_list), safe=False)

def common_friends(request):
    people_index_list = request.GET.getlist('people_id', '')
    if len(people_index_list) != 2 :
        error = {'status': 'Failed', 'message': 'There has to be 2 people id'}
        return JsonResponse(error, safe=False, status=400)
    api_response = {'people_details':[], 'common_friends': []}
    common_friend_list = []
    for index in people_index_list:
        people_id = 0
        try:
            people_id = int(index)
        except ValueError:
            error = {'status': 'Failed', 'message': 'people_id has to be integer'}
            return JsonResponse(error, safe=False, status=400)
        try:
            people = People.objects.get(pk=people_id)
        except People.DoesNotExist:
            error = {'status': 'Failed', 'message': f'people with id {people_id} does not exist'}
            return JsonResponse(error, safe=False, status=400)
        api_response['people_details'].append({
                'name': people.name,
                'age': people.age,
                'address': people.address,
                'phone': people.phone})
        common_friend_list.append(people.friend)
    friend_list_a = json.loads(common_friend_list[0])
    friend_list_b = json.loads(common_friend_list[1])
    common_friends_id = [ a for a in friend_list_a if a in friend_list_b]
    common_friends = People.objects.filter(
        pk__in = common_friends_id, 
        eye_color = 'brown', 
        has_died = False)
    api_response['common_friends'] = serialize('python', common_friends)
    return JsonResponse(api_response)

def people_details(request):
    people_id_parameter = request.GET.get('people_id', '')
    people_id = 0
    try:
        people_id = int(people_id_parameter)
    except ValueError:
        error = {'status': 'Failed', 'message': 'people_id has to be integer'}
        return JsonResponse(error, safe=False, status=400)
    try:
        people = People.objects.get(pk=people_id)
    except People.DoesNotExist:
        error = {'status': 'Failed', 'message': f'people with this id {people_id} does not exist'}
        return JsonResponse(error, safe=False, status=400)
    
    api_response = {"username": people.name, 
    "age": people.age, 
    "fruits": people.fruit, 
    "vegetables": people.vegetable}
    return JsonResponse(api_response)