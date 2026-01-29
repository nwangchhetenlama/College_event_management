from django.shortcuts import render,redirect
from .models import Event,EventRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import date
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
# def base(request):
#     return render(request,'base.html')
from .form import Eventform
from django.contrib.auth.decorators import login_required
from .models import EventRegistration


def event_list(request):

    events=Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request,'events/event_list.html',context={'events':events})

@login_required(login_url='login')
def event_detail(request,id):

    event=Event.objects.get(id=id)
    already_registered=EventRegistration.objects.filter(user=request.user,event=event).exists()
    total_participants=EventRegistration.objects.filter(event=event).count()

    if request.method=='POST':


        if event.registration_deadline < date.today():
            messages.error(request, "Registration deadline has passed.")
        elif already_registered:
            messages.error(request,"the user is already registered.")

        elif total_participants>=event.max_participants:
            messages.error(request,"participants are filled.")

        else:
            EventRegistration.objects.create(user=request.user,event=event)
            send_mail(subject="Event registration successful",message=f'''Hello {request.user.username},
                    You have successfully registered for the event:

                    Event: {event.title}
                    Date: {event.date}
                    Time: {event.time}
                    Venue: {event.venue}

                    Thank you for participating!
                    ''',
                    from_email=None,
                    recipient_list=[request.user.email],
                    fail_silently=True
                    
            )
            messages.success(request,"The user is registered for this event") 

        return redirect('event_detail', id=event.id)





    return render(request,'events/event_detail.html',context={'event':event,'already_registered':already_registered,'total_participants':total_participants})


@staff_member_required(login_url='login')
def createEvent(request):

    form = Eventform()

    if request.method == 'POST':
        form = Eventform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect('/')

    context = {'form': form}
    return render(request, 'events/create_event.html', context)



@staff_member_required(login_url='login')
def updateEvent(request,id):
    event=Event.objects.get(id=id)
    form=Eventform(instance=event)


    if request.method=='POST':
        form=Eventform(request.POST,request.FILES,  instance=event)
        
        if form.is_valid():
            form.save()
            return redirect("/")


    context={'form':form}
    return render(request,'events/create_event.html',context)

@staff_member_required(login_url='login')
def deleteEvent(request,id):

    event=Event.objects.get(id=id)
    if request.method=='POST':
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("/")

    return render(request,'events/delete.html',{'event':event})




@login_required(login_url='login')
def profile(request):
    registrations = EventRegistration.objects.filter(
        user=request.user
    ).select_related('event').order_by('-registered_at')

    context = {
        'registrations': registrations
    }
    return render(request, 'events/profile.html', context)
