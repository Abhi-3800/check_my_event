from django import forms
from django.forms import ModelForm
from .models import Venue, Event

class VenueForm(ModelForm):
	class Meta:
		model = Venue
		# fields = "__all__"
		fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
		labels = {
			"name": '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': ''
		}
		widgets = {
			"name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter venue name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Enter venue address"}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter the venue zip-code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Website'}),
			'email_address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Your Email'})
		}

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
		labels = {
			"name": '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Select Venue',
			'manager': 'Select Manager',
			'attendees': '',
			'description': ''
		}
		widgets = {
			"name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter event name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder': "Enter event date"}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Enter the event venue'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Event manager'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Event attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Event description'})
		}
