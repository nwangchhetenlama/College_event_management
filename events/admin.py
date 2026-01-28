from django.contrib import admin

# Register your models here.

from .models import Event,EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'time',
        'venue',
        'max_participants',
        'registration_deadline',
    )
    search_fields = ('title', 'venue')
    list_filter = ('date',)



@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'registered_at')
    list_filter=('event',)

    
