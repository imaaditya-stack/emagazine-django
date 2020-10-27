from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, Event


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class ValidateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'