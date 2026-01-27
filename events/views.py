from django.shortcuts import render,redirect
from .models import Event,EventRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import date
# def base(request):
#     return render(request,'base.html')



def event_list(request):

    events=Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request,'events/event_list.html',context={'events':events})

@login_required
def event_detail(request,id):

    event=Event.objects.get(id=id)
    already_registered=EventRegistration.objects.filter(user=request.user,event=event).exists()
    total_participants=EventRegistration.objects.filter(event=event).count()

    if request.method=='POST':
        if already_registered:
            messages.error(request,"the user is already registered.")

        elif total_participants>=event.max_participants:
            messages.error(request,"participants are filled.")

        else:
            EventRegistration.objects.create(user=request.user,event=event)
            messages.success(request,"The user is registered for this event") 

        return redirect('event_detail', id=event.id)





    return render(request,'events/event_detail.html',context={'event':event,'already_registered':already_registered,'total_participants':total_participants})
