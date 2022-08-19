

from sqlite3 import Timestamp
from django.contrib import admin
from . import models

from pages.models import Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('TicketNum','dept','timestamp','due_Date','title',)

admin.site.register(Ticket, TicketAdmin)