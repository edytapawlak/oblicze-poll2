from django.shortcuts import render
from activities.models import Lecture, Status 
from abstract_contest.models import ChoosedLecture

from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False
    return user_passes_test(in_groups)

# Create your views here.
@group_required('admins','Komisja')
def choose_lectures(request):
    if (request.method == "POST"):
        print(request.POST.getlist('correct'))
        ChoosedLecture.objects.all().delete()
        for lecture_id in request.POST.getlist('correct'):
            lect = Lecture.objects.get(id = lecture_id)
            print(lect)
            l = ChoosedLecture(lecture = lect)
            l.save()    

    accepted_lectures = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
    uncorrect_lectures = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na poprawę")) 
    choosed = Lecture.objects.filter(choosedlecture__in = ChoosedLecture.objects.all())
    print(choosed)
    args = {'correct_lectures': accepted_lectures, 'uncorrect_lectures': uncorrect_lectures, 'choosed': choosed }
    return render(request, 'abstract_contest/view_lectures.html', args)

def choose_posters(request):
    pass
