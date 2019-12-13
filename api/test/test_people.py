from django.test import TestCase
from api.models import People

class CompanyTestCase(TestCase):
    def setUp(self):
        People.objects.create(
            people_id = 1001,
            has_died = True,
            age = 40,
            eye_color = 'green',
            name = 'John Doe',
            company_id = 101,
            fruit = "['orange', 'apple', 'banana', 'strawberry']",
            vegetable = "",
            friend = "['1', '2']",
            address = 'test address',
            phone = 'test phone',
            )
        People.objects.create(
            people_id = 1002,
            has_died = True,
            age = 40,
            eye_color = 'green',
            name = 'John Doe',
            company_id = 101,
            fruit = "['orange', 'apple', 'banana', 'strawberry']",
            vegetable = "",
            friend = "['1', '2']",
            address = 'test address',
            phone = 'test phone',
            )

    def test_company_exists(self):
        people_1 = People.objects.get(pk=1001)
        people_2 = People.objects.get(pk=1002)
        self.assertEquals(str(people_1), "People{people_id: 1001, has_died: True,eye_color: green,name: John Doe,company_id: 101,fruit: ['orange', 'apple', 'banana', 'strawberry'],vegetable: ,address: test address,phone: test phone,friend: ['1', '2'],}")
        self.assertEquals(str(people_2), "People{people_id: 1002, has_died: True,eye_color: green,name: John Doe,company_id: 101,fruit: ['orange', 'apple', 'banana', 'strawberry'],vegetable: ,address: test address,phone: test phone,friend: ['1', '2'],}")

    def test_company_number(self):
        number_of_people = People.objects.count()
        self.assertGreater(number_of_people, 0)