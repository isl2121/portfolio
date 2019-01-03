from django import forms

class mailform(forms.Form):
        name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Name'}))
        mail = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Email'}))
        subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Subject'}))
        message = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '* Message'}))

