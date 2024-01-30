from django.contrib import admin

from market.conversation.models import ConversationMessage, Conversation


# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    pass