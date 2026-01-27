from django.shortcuts import render
from .models import Event
# Create your views here.
from datetime import date
# def base(request):
#     return render(request,'base.html')



def event_list(request):

    events=Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request,'events/event_list.html',context={'events':events})


def event_detail(request,id):

    event=Event.objects.get(id=id)

    return render(request,'events/event_detail.html',context={'event':event})

    