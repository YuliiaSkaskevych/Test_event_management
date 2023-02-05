# Test_ivent_management
Task: To create event management sustem

Quick Start

To get this project up and running locally on your computer:

    1. Set up the Python development environment. We recommend using a Python virtual environment.
    2. Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py test # Run the standard tests. These should all pass.
    python3 manage.py createsuperuser # Create a superuser
    python3 manage.py runserver

    3. Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
    4. Create a few test objects of each type.
    5. Open tab to http://127.0.0.1:8000/event/ to see the main site, with your new objects.

Description:

1. Develop an event management system that will receive POST data
requests in the format
{
"event_type": <event_type.name>
"info": <any json>
"timestamp": <datetime>
}

This data will be stored in the Event model.
Event {
id - uuid field (primary key),
user -pk field,
event_type - pk field,
info - JSON field,
timestamp - datetime field,
created_at - auto datetime field
}
And models EventType {
id - int,
name - char(256)
}
2. If the incoming event_type is not in the database, then create it.
3. Requests must come authenticated, that is, with a token in the header.
To do this, use the rest_framework.authtoken module
4. Add Django admin for both models. For the Event model, add
filtering by event_type and timestamp.
5. Cover the Post request with tests, the choice of library is up to you
6. Add a README.md file with a description and how to start the service
7. Requirements:
- Django;
- DRF;
 - database - SQLite;

