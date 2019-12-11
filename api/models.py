from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Company{{company_id: {self.company_id}, name: {self.name}}}'

class People(models.Model):
    people_id = models.CharField(max_length=30)
    index = models.AutoField(primary_key=True)
    guid = models.CharField(max_length=100)
    has_died = models.BooleanField(default=False)
    balance = models.CharField(max_length=100, default=None, null=True)
    picture = models.CharField(max_length=500, default=None, null=True)
    age = models.IntegerField(default=None, null=True)
    eyeColor = models.CharField(max_length=20,default=None, null=True)
    name = models.CharField(max_length=100, default='')
    company_id = models.IntegerField(default=None, null=True)
    fruit = models.CharField(max_length=200, default=None, null=True)
    vegetable = models.CharField(max_length=200, default=None, null=True)
    
    def __str__(self):
        return (f'People{{people_id: {self.people_id}, '
        f'index: {self.index},'
        f'guid: {self.guid},'
        f'has_died: {self.has_died},}}')

class Friendship(models.Model):
    friendship_id = models.AutoField(primary_key=True)
    self_id = models.ForeignKey(default=0, null=False, to='People', on_delete=models.CASCADE)
    friend_id = models.ForeignKey(default=0, null=False, to='People', on_delete=models.CASCADE)

