from django.shortcuts import render
from activities.models import Lecture, Status 
from abstract_contest.models import ChoosedLecture

# Create your views here.
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
