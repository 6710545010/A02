from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import RoomData, Reservation

class RegistorForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["room"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = RoomData.objects.filter(room_available=True, room_hour__gt=0)


    

