from django.test import TestCase
from api.models import Company

class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(company_id=101, name="test1 co.")
        Company.objects.create(company_id=102, name="test2 co.")

    def test_company_exists(self):
        company_1 = Company.objects.get(pk=101)
        company_2 = Company.objects.get(pk=102)
        self.assertEquals(str(company_1), 'Company{company_id: 101, name: test1 co.}')
        self.assertEquals(str(company_2), 'Company{company_id: 102, name: test2 co.}')

    def test_company_number(self):
        number_of_company = Company.objects.count()
        self.assertGreater(number_of_company, 0)