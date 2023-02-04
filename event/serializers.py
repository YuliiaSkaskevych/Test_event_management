from .models import Event, EventType
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['event_type', 'info', 'timestamp']


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = ['name']

