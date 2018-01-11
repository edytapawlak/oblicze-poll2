from django.shortcuts import render
from activities.models import Lecture

# Create your views here.
def view_poll(request):
    lecture_list = Lecture.objects.all()
    print(lecture_list) 
    return render(request, 'poll/view_poll.html', {'lectures': lecture_list})

def edit_poll(request):
    pass
