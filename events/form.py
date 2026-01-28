
from django.forms import ModelForm

from .models import Event

class Eventform(ModelForm):
    
    class Meta:
        model=Event
        fields='__all__'

        exclude=['created_at']


