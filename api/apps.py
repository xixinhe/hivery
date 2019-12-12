from django.apps import AppConfig
import json

class ApiConfig(AppConfig):
    name = 'api'

    # def ready(self):
    #     from .models import Company, People
    #     print('This is test starting up function')
    #     Company = self.get_model('Company')
    #     People = self.get_model('People')
    #     fruits_list = []
    #     if People.objects.count() > 0:
    #         People.objects.all().delete()
    #     if Company.objects.count() > 0:
    #         Company.objects.all().delete()
        
    #     with open('./fruit_list.json') as fruit_list_json:
    #         fruits_list = json.load(fruit_list_json)

    #     with open('./companies.json') as companies_file:
    #         companies = json.load(companies_file)
    #         for company in companies:
    #             Company(company_id=company['index'], name=company['company']).save()

    #     with open('./people.json') as people_file:
    #         peoples = json.load(people_file)
    #         for people in peoples:
    #             food = people['favouriteFood']
    #             fruit = [a for a in food if a in fruits_list]
    #             vegetable = [a for a in food if a not in fruit]
    #             friend=[a['index'] for a in people['friends']]
    #             People(
    #                 people_id=people['_id'], 
    #                 index=people['index'],
    #                 guid=people['guid'],
    #                 has_died=people['has_died'],
    #                 balance=people['balance'],
    #                 picture=people['picture'],
    #                 age=people['age'],
    #                 eyeColor=people['eyeColor'],
    #                 name=people['name'],
    #                 company_id=people['company_id'],
    #                 vegetable=vegetable,
    #                 fruit=fruit,
    #                 address=people['address'],
    #                 phone=people['phone'],
    #                 friend=json.dumps(friend)).save()

