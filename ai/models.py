from django.db import models

from ai.types import AICategory
from users.models import User


# Create your models here.
class Message(models.Model):
    prompt = models.CharField(blank=False, null=False)
    request = models.TextField(blank=False, null=False)
    response = models.JSONField(blank=False, null=False)
    category = models.CharField(blank=True, null=True,
                                choices=[(category.value, category.value.capitalize()) for category in AICategory])

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
