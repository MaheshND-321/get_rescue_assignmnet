from django.http import HttpResponse
from django.shortcuts import render
from .models import Issue, Agent1,Agent2,Agent3,Agent4,Agent5, Mechanic
import random


i=0

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
        j=i%5
        issue_table = Issue(issue_id=iss_id,user_id=usr_id,location=location,problem=problem,time=time,status=status)
        issue_table.save()
        match  j:
            case 1:
                agent_table = Agent1(queue=usr_id)
            case 2:
                agent_table = Agent2(queue=usr_id)
            case 3:
                agent_table = Agent3(queue=usr_id)
            case 4:
                agent_table = Agent4(queue=usr_id)
            case 5:
                agent_table = Agent5(queue=usr_id)
            
        agent_table.save()
        print(iss_id)
        print(usr_id)
        print(location)
        print(problem)
        print(time)
        print(status)
        return HttpResponse("Submitted")
    else:
        return render(request, 'index.html')

