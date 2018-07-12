from django import forms
from django.core.validators import URLValidator
from .models import Urls

class UrlsForm(forms.ModelForm):
	url = forms.CharField(label = 'Submit URl', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your URL',
        } ))


	class Meta:
		model = Urls
		fields = ('url', )


class UrlsFormNew(forms.ModelForm):
	url = forms.CharField(label = 'Submit URl', widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Your URL',
			} ))
	short_link = forms.CharField(label = 'Short link', widget = forms.TextInput(
		attrs = {
			'class':'form-control',
			'placeholder': 'Short link'
		}))

	class Meta:
		model = Urls
		fields = ('url', 'short_link', 'text', 'active', )