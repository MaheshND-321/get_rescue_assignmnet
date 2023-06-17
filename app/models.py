from django.db import models 
from django.contrib.auth.models import User

choice=(
    ('1','inque'),
    ('2','assigned'),
    ('3','dispatched'),
)


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    user_name = models.CharField(max_length=100,default=0)
    location = models.CharField(max_length=100,default=0)
    problem = models.TextField(default=0)
    time = models.CharField(max_length=100,default=0)
    status = models.CharField(max_length=100,choices=choice,null=False,default='inque')


class Agent1(models.Model):
    agent_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    queue = models.CharField(max_length=100,choices=choice,null=False,default='inque')

class Agent2(models.Model):
    agent_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    queue = models.CharField(max_length=100,choices=choice,null=False,default='inque')

class Agent3(models.Model):
    agent_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    queue = models.CharField(max_length=100,choices=choice,null=False,default='inque')

class Agent4(models.Model):
    agent_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    queue = models.CharField(max_length=100,choices=choice,null=False,default='inque')

class Agent5(models.Model):
    agent_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100,default=0)
    queue = models.CharField(max_length=100,choices=choice,null=False,default='inque')



class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

