from django.db import models

# Create your models here.
class Company(models.Model):
    index = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Company{{index: {self.index}, name: {self.name}}}'

class People(models.Model):
    people_id = models.CharField(max_length=30)
    index = models.IntegerField()
    guid = models.CharField(max_length=100)
    has_died = models.BooleanField(default=False)
    balance = models.CharField(max_length=100)
    picture = models.CharField(max_length=500)
    age = models.IntegerField(null=False)
    eyeColor = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    company_id = models.IntegerField()

    def __str__(self):
        return (f'People{{people_id: {self.people_id}, '
        f'index: {self.index},'
        f'guid: {self.guid},'
        f'has_died: {self.has_died},}}')