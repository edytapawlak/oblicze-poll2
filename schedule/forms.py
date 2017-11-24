from django import forms
from activities.models import Lecture 
from schedule.models import Schedule

class ScheduleForm(forms.ModelForm):

    lecture_list = forms.ModelChoiceField(queryset= Lecture.objects.all())
    class Meta:
        model = Schedule
        fields = ('start', 'end', 'date', 'place', )

