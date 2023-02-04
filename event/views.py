from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Event, EventType
from .serializers import EventSerializer, EventTypeSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def event_create(self, serializer):
        serializer.save(user=self.request.user)


class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def new_type_create(self, serializer):
        serializer.save()
