# get_rescue_assignmnet


## Model part has:

Issue: This model represents an issue that needs to be addressed. It has the following fields:

issue_id: Auto-generated primary key for the issue.
user_id: CharField to store the user's ID.
user_name: CharField to store the user's name.
location: CharField to store the location of the issue.
problem: TextField to describe the problem.
time: CharField to store the time of the issue.
status: CharField with choices defined by the choice tuple. It represents the current status of the issue, with a default value of 'inque'.
Agent1, Agent2, Agent3, Agent4, Agent5: These models represent different agents who can handle issues. Each model has the following fields:

agent_id: Auto-generated primary key for the agent.
user_id: CharField to store the agent's ID.
queue: CharField with choices defined by the choice tuple. It represents the current queue status of the agent, with a default value of 'inque'.
Mechanic: This model represents a mechanic who can handle repairs. It has the following fields:

mechanic_id: Auto-generated primary key for the mechanic.
availability: BooleanField to indicate the availability of the mechanic, with a default value of True.

## command to check the changes made in models:
Python manage.py makemigrations

## command to push all the changes into the database:
python manage.py migrate

## command to run the project:
python manage.py runserver

after the project is launched succesfully click on control + Starting development server at http://127.0.0.1:8000/ 
or Enter the port number in webbrowser as http://127.0.0.1:8000/ 

## To check out the tables stored in the Database:
enter /admin in url section to enter the admin panel
 
