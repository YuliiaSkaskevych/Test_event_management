from django.db import models
from rest_framework.authtoken.models import Token


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.UUIDField
    event_type = models.UUIDField
    info = models.JSONField
    timestamp = models.DateTimeField
    created_at = models.DateTimeField(auto_now_add=True)


class EventType(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=256)
