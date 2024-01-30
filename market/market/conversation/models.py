from django.contrib.auth import get_user_model
from django.db import models

from market.item.models import Item

UserModel = get_user_model()


# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='conversations'
    )
    members = models.ManyToManyField(
        UserModel,
        related_name='conversations'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at', ]


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name='messages'
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='created_messages'
    )
