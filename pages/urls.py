from django.urls import path 
from pages import views

urlpatterns = [
    path('',views.home),
    path('raise-ticket/',views.raiseticket),
    path('view-ticket-status/',views.viewticket),
    path('view-ticket-status/<slug:numid>',views.viewstatus, name='viewstatus'),
]