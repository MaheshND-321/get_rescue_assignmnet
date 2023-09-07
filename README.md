# GetRecuse Project README

Welcome to the README file for the GetRecuse project! This project aims to provide assistance to individuals facing vehicle-related issues such as punctures, fuel overruns, and other problems. Users can submit their issues through a form, and the system assigns these issues to available agents. The agents then allocate appropriate mechanics who can efficiently address the reported vehicle problems. This project streamlines the process of providing timely help to people in need of vehicle rescue.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The GetRecuse project offers a platform for individuals to seek assistance for vehicle-related issues. By utilizing a user-friendly form, users can report their vehicle problems such as punctures or fuel overruns. The system assigns these issues to available agents who, in turn, select appropriate mechanics located near the users with the vehicle problems. This project is a practical solution to provide prompt help to those encountering vehicle-related emergencies.

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

## Features

The GetRecuse project includes the following features:

- **Issue Submission**: Users can submit their vehicle-related issues through a form.

- **Agent Assignment**: Available agents are assigned to address the reported issues.

- **Mechanic Allocation**: Agents allocate suitable mechanics who are available and nearby.

- **Real-time Assistance**: The project aims to provide timely help to individuals facing vehicle problems.

## Installation

To set up the GetRecuse project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/getrecuse.git
   ```

2. Navigate to the project directory:
   ```bash
   cd getrecuse
   ```

3. Install the required dependencies (if applicable).

4. Configure the necessary settings for the form, agent assignment, and mechanic allocation.

5. Run the project application:
   ```bash
   python manage.py runserver
   ```

6. Access the project through your web browser at `http://localhost:8000`.

7. ## command to check the changes made in models:
Python manage.py makemigrations

## command to push all the changes into the database:
python manage.py migrate

## command to run the project:
python manage.py runserver

after the project is launched succesfully click on control + Starting development server at http://127.0.0.1:8000/ 
or Enter the port number in webbrowser as http://127.0.0.1:8000/ 

## To check out the tables stored in the Database:
enter /admin in url section to enter the admin panel

## Usage

1. Launch the project application.

2. Users fill out the form with details of their vehicle issue.

3. The system assigns the issue to an available agent.

4. The agent selects an appropriate mechanic based on the user's location and problem.

5. The assigned mechanic responds to the issue and provides assistance.

## Contributing

We welcome contributions to the GetRecuse project! If you wish to contribute, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository.

5. Create a pull request to the main repository's `develop` branch, explaining your changes.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to explore, utilize, and contribute to the GetRecuse project. If you encounter any issues or have suggestions, please create an issue on the repository. Help is on the way! 🚗🔧
 
