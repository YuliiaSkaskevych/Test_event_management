from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

User = get_user_model()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class EventType(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    info = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.event_type} by {self.user}'
