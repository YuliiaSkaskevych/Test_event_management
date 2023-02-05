import pytest
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_201_CREATED
from .models import Event, EventType
User = get_user_model()


@pytest.mark.django_db
def test_create_event_db():
    User.objects.create_user(username='admin', email='example@mail.com', password='1234567890')
    EventType.objects.create(name='12345')
    Event.objects.create(user='admin', event_type='12345', timestamp='2023-09-04', info=[{
            "user": 1,
            "event_type": '12345',
            "timestamp": '2023-09-04'}])


@pytest.mark.django_db
def test_create_event(events, authenticated_user):
    events(_quantity=1)
    url = 'http://127.0.0.1:8001/event/'
    event = {'event': [{
                "user": 1,
                "event_type": '12345',
                "timestamp": '2023-09-04',
                "info": [{
                "user": 1,
                "event_type": '12345',
                "timestamp": '2023-09-04'}]
            }]}
    resp = authenticated_user.post(url, event, content_type='application/json')
    print(resp.json())
    assert resp.status_code == HTTP_201_CREATED
