from django import forms
from accomodation.models import Dinner, Hostel 
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

ALL_DATES = (('0', '11/11/11'), ('1', '12/11/11'), ('2', '13/11/11'),)

class AccomodationForm(forms.ModelForm):

    date = forms.MultipleChoiceField(
            choices=ALL_DATES,
            widget = forms.CheckboxSelectMultiple,
            required=False)

#    date = forms.DateField(widget=DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))    
    class Meta:
        model = Hostel
        fields = {'date' }


class DinnerForm(forms.ModelForm):
#    date = forms.DateField(widget=DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))    
#    date= forms.MultipleChoiceField(
#            choices=ALL_DATES, 
#            widget = forms.CheckboxSelectMultiple,
#            required=False)

    remark = forms.CharField(required = False)
    class Meta:
        model = Dinner
        fields = ( 'remark', )
#        widgets = {'date': forms.DateInput()}


