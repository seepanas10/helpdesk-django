from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pages.models import Ticket
from pages.forms import TicketForm, StatusForm

# Create your views here.

def home(request):
    return render(request, 'base.html')

def raiseticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            form.send()
            tkt = Ticket.objects.latest('timestamp')
            return render(request,'success.html',{'tkt':tkt})
            
    else:
        form = TicketForm()
    
    return render(request,'raiseticket.html',{'form': form}
    )

def viewticket(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            ticketid = request.POST.get('ticketid')
            return redirect('viewstatus', numid=ticketid)
            
    else:
        form = StatusForm()
    
    return render(request,'viewticket.html',{'form': form}
    )
    
def viewstatus(request,numid):
    num = int(numid)%1000
    status = Ticket.objects.get(id=num)
    return render(request,'viewstatus.html',{'status': status})