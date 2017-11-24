from django.shortcuts import render, redirect
from schedule.forms import ScheduleForm
from activities.models import Lecture
from schedule.models import Schedule

# Create your views here.

def view_schedule(request):
    if (request.method == 'POST'):
        form = ScheduleForm(request.POST)
        if (form.is_valid()):
            lecture = form.cleaned_data['lecture_list']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            place = form.cleaned_data['place']
            date = form.cleaned_data['date']
#            print(str(lecture))
#            created_schedule = form.save()
            schedule, created = Schedule.objects.get_or_create(start = start, end = end, place = place, date = date)
            Lecture.objects.filter(pk = lecture.pk).update(schedule = schedule)
            return redirect('/schedule')
    else:
        form = ScheduleForm()
        args = {'form': form}
        return render(request, 'schedule/add_schedule.html', args)
