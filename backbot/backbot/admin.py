from django.contrib import admin

from clients.models import UserExchange, Exchange

admin.site.register(UserExchange)
admin.site.register(Exchange)