from django import forms
from poll.models import Status 

class StatusForm(forms.ModelForm):

    class Meta:
        model = Status 
        fields = ('poll_status', )

