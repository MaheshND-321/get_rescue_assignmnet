from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Issue, Agent1,Agent2,Agent3,Agent4,Agent5, Mechanic
import random
from django.contrib import messages


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
        j=j+1
        issue_table = Issue(issue_id=iss_id,user_id=usr_id,user_name=user_name,location=location,problem=problem,time=time,status=status)
        issue_table.save()
        match  j:
            case 1:
                agent_table = Agent1(user_id=usr_id,queue=status)
            case 2:
                agent_table = Agent2(user_id=usr_id,queue=status)
            case 3:
                agent_table = Agent3(user_id=usr_id,queue=status)
            case 4:
                agent_table = Agent4(user_id=usr_id,queue=status)
            case 5:
                agent_table = Agent5(user_id=usr_id,queue=status)
            
        agent_table.save()
        messages.success(request, 'Issue submitted successfully!')
        # print(iss_id)
        # print(usr_id)
        # print(location)
        # print(problem)
        # print(time)
        # print(status)
        # return HttpResponse("Submitted")
        return redirect('/')
    else:
        return render(request, 'index.html')

