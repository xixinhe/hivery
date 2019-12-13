from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Company{{company_id: {self.company_id}, name: {self.name}}}'

class People(models.Model):
    people_id = models.AutoField(primary_key=True)
    has_died = models.BooleanField(default=False)
    age = models.IntegerField(default=None, null=True)
    eye_color = models.CharField(max_length=20,default=None, null=True)
    name = models.CharField(max_length=100, default='')
    company_id = models.IntegerField(default=None, null=True)
    fruit = models.CharField(max_length=200, default=None, null=True)
    vegetable = models.CharField(max_length=200, default=None, null=True)
    friend = models.CharField(max_length=100, default='', null=True)
    address = models.CharField(max_length=200, default='', null=True)
    phone = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return (f'People{{people_id: {self.people_id}, '
        f'has_died: {self.has_died},'
        f'eye_color: {self.eye_color},'
        f'name: {self.name},'
        f'company_id: {self.company_id},'
        f'fruit: {self.fruit},'
        f'vegetable: {self.vegetable},'
        f'address: {self.address},'
        f'phone: {self.phone},'
        f'friend: {self.friend},}}')
