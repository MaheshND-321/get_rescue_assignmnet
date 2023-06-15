from django.db import models 
from django.contrib.auth.models import User

class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    problem = models.TextField()
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=20)


class Agent1(models.Model):
    agent_id = models.AutoField(primary_key=True)
    queue = models.CharField(max_length=100)

class Agent2(models.Model):
    agent_id = models.AutoField(primary_key=True)
    queue = models.CharField(max_length=100)

class Agent3(models.Model):
    agent_id = models.AutoField(primary_key=True)
    queue = models.CharField(max_length=100)

class Agent4(models.Model):
    agent_id = models.AutoField(primary_key=True)
    queue = models.CharField(max_length=100)

class Agent5(models.Model):
    agent_id = models.AutoField(primary_key=True)
    queue = models.CharField(max_length=100)



class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

