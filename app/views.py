from django.http import HttpResponse
from django.shortcuts import render
from .models import Issue, Agent, Mechanic
import random


i=1

def index(request):
    if request.method == "POST":
        problem = request.POST['problem']
        location = request.POST['location']
        time = request.POST['time']
        user_name = request.POST['user_name']
        # i=random.randint(1, 100)
        global i
        i=i+1
        iss_id=i
        usr_id="usr_id"+str(i)
        status='Inque'

        issue_table = Issue(issue_id=iss_id,user_id=usr_id,location=location,problem=problem,time=time,status=status)
        issue_table.save()
        print(iss_id)
        print(usr_id)
        print(location)
        print(problem)
        print(time)
        print(status)
        return HttpResponse("Submitted")
    else:
        return render(request, 'index.html')

