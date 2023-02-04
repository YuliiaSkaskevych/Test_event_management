from django.contrib import admin
from .models import EventType, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ['user', 'event_type', 'timestamp']
    list_filter = ['event_type', 'timestamp']


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    fields = ['name']
