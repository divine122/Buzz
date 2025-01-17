from django import forms

class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Type a message here...'}))
