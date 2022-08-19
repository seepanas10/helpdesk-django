from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Ticket(models.Model):

    class TicketDept(models.TextChoices):
        ACCOUNTS = 'ACC'
        MAINTENNANCE = 'MAINT'
        INFRASTRUCTURE = 'INFRA'
    
    dept = models.fields.CharField(choices=TicketDept.choices, max_length=5)

    class TicketPriority(models.TextChoices):
        HIGH = 'HIGH'
        MEDIUM = 'MED'
        LOW = 'LOW'

    priority = models.fields.CharField(choices=TicketPriority.choices, max_length=5)

    due_Date = models.fields.DateField()
    title = models.fields.CharField(max_length=500)
    description = models.fields.TextField()
    file_Upload = models.FileField(upload_to = 'uploads/', blank=True, help_text='Not Mandatory')
    timestamp = models.fields.DateTimeField(auto_now_add=True,auto_now=False)

    class TicketStatus(models.TextChoices):
        OPEN = 'OPEN'
        WORKING = 'WORKING'
        REOPENED = 'REOPENED'
        CLOSED = 'CLOSED'

    status = models.fields.CharField(choices=TicketStatus.choices, max_length=10, default=TicketStatus.OPEN)

    @property
    def TicketNum(self):
        if self.dept == 'ACC':
            return 22071000+self.id
        elif self.dept == 'MAINT':
            return 22072000+self.id
        elif self.dept == 'INFRA':
            return 22073000+self.id
        
    

