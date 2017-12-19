from django.shortcuts import render, redirect
from activities.forms import LectureForm, PosterForm
from activities.models import Author, Status
from utils import is_tex_valid

# Create your views here.
def register_lecture(request):
    author, created = Author.objects.get_or_create(user = request.user)
    lecture = author.lecture_id
#    print(lecture)
    if request.method == 'POST':
        form = LectureForm(request.POST, instance = lecture)
        if form.is_valid():
            #sprawdzenie czy abstrakt jest poprawny
            created_lect = form.save()
            created_lect.tags = form.cleaned_data['tags']
            print(str(created_lect.tags))
            try:
                is_tex_valid(form.cleaned_data['abstract'])
                created_lect.status = Status.objects.get(title = "Czeka na akceptację") 
            except ValueError:
                created_lect.status = Status.objects.get(title = "Czeka na poprawę")
            created_lect.save()
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
            created_poster= form.save(commit = False)
            created_poster.tags = form.cleaned_data['tags']
             #sprawdzenie czy abstrakt jest poprawny
            try:
                is_tex_valid(form.cleaned_data['abstract'])
                created_poster.status = Status.objects.get(title = "Czeka na akceptację") 
            except ValueError:
                created_poster.status = Status.objects.get(title = "Czeka na poprawę")
            created_poster.save()
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

  
