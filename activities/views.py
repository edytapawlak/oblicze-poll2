from django.shortcuts import render, redirect
from activities.forms import LectureForm, PosterForm
from activities.models import Author

# Create your views here.
def register_lecture(request):
    author, created = Author.objects.get_or_create(user = request.user)
    lecture = author.lecture_id
#    print(lecture)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance = lecture)
        if form.is_valid():
            created_lect = form.save()
            updated_value = {'lecture_id': created_lect}
            author, created = Author.objects.update_or_create(user = request.user, defaults = updated_value)
            return redirect('/activities/view_lecture')
    else:
        form = LectureForm(instance = lecture)
        args = {'form': form}
        #args = {'lecture': lecture }
        return render(request, 'activities/edit_lecture.html', args)

def view_lecture(request):
    author, created = Author.objects.get_or_create(user = request.user)
    lecture = author.lecture_id
    args = {'lecture': lecture}
    return render(request, 'activities/view_lecture.html', args)

def edit_poster(request):
    author, created = Author.objects.get_or_create(user = request.user)
    poster = author.poster_id
    print(poster)
    if request.method == 'POST':
        form = PosterForm(request.POST, instance = poster)
        if form.is_valid():
            created_poster= form.save()
            updated_value = {'poster_id': created_poster}
            author, created = Author.objects.update_or_create(user = request.user, defaults = updated_value)
            return redirect('/activities/view_poster')
    else:
        form = LectureForm(instance = poster)
        args = {'form': form}
        #args = {'lecture': lecture }
        return render(request, 'activities/edit_lecture.html', args)

def view_poster(request):
    author, created = Author.objects.get_or_create(user = request.user)
    poster = author.poster_id
    args = {'poster': poster}
    return render(request, 'activities/view_poster.html', args)

  
