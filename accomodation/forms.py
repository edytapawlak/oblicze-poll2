from django import forms
from accomodation.models import Dinner
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class AccomodationForm(forms.ModelForm):
    hostel = forms.CharField()

class DinnerForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))    
    class Meta:
        model = Dinner
        fields = ('remark', 'date','vege')
#        widgets = {'date': forms.DateInput()}
