from django import forms
from django.core.mail import send_mail

from pages.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('status',)

    def get_info(self):

        cl_data = super().clean()

        deptname = cl_data.get('dept')
        prty = cl_data.get('priority')
        ddate = cl_data.get('due_Date')
        heading = cl_data.get('title')
        message = cl_data.get('description')

        msg = f'There is a new complaint in the {deptname} Deaprtment with {prty} priority and the due date for the same is {ddate})'
        msg += f'\nThe complaint goes as follows with the title'
        msg += f'\n"{heading}"\n\n'
        msg += f'{message}'

        return heading, msg, deptname

    def send(self):

        subject, msg, deptname = self.get_info()
        if deptname == 'ACC':
                to_list = ['seepana.s10@gmail.com']
        elif deptname == 'MAINT':
                to_list = ['gvpce17194@gmail.com']
        else:
            to_list = ['213040067@iitb.ac.in']

        send_mail(
            subject=f'New Help Ticket Raised',
            message=msg,
            from_email = 'sushanthseepana2000@gmail.com',
            recipient_list=to_list,
            fail_silently=False,
        )

class StatusForm(forms.Form):
    ticketid = forms.IntegerField(label='Please Enter your Ticket ID')