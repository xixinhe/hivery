from django.apps import AppConfig
import json

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        from .models import Company, People
        print('This is test starting up function')
        Company = self.get_model('Company')

        if Company.objects.count() <= 0:
            with open('./companies.json') as companies_file:
                companies = json.load(companies_file)
                for company in companies:
                    Company(index=company['index'], name=company['company']).save()

        print(Company.objects.count())

        # People = self.get_model('People')

        # if People.objects.count() <= 0:
        #     with open('./people.json') as people_file:
        #         peoples = json.load(people_file)
        #         for people in peoples:
        #             People(
        #                 people_id=people['_id'], 
        #                 index=people['index'],
        #                 guid=people['guid'],
        #                 has_died=people['has_died']).save()

        # print(People.objects.all())