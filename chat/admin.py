from django.contrib import admin
from chat.models import(
    Message,
)

class Messageadmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'message', 'is_read','updated_on')
admin.site.register(Message,Messageadmin) 
