from django.contrib import admin

# Register your models here.

from .models import Event

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
    