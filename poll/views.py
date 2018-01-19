from django.db.models import Sum
from django.shortcuts import render, redirect
from activities.models import Lecture, Poster, Author
from poll.forms import StatusForm
from poll.models import LectureRating, PosterRating, Status

def view_poll(request):
    ratings = list(LectureRating.objects.filter(user = request.user).order_by('-rate'))
    lect_rate_tuples = [(x.lecture, x.rate,  list(Author.objects.filter(lecture_id = x.lecture))) for x in ratings]
    poster_ratings = list(PosterRating.objects.filter(user = request.user).order_by('-rate'))
    poster_rate_tuples = [(x.poster, x.rate,  list(Author.objects.filter(poster_id = x.poster))) for x in poster_ratings]
    return render(request, 'poll/poll_summary.html', {'lectures': lect_rate_tuples, 'posters': poster_rate_tuples, 'user': request.user }
)
def poll(results, user):
    first = '' 
    second = ''
    third = ''
    LectureRating.objects.filter(user = user).delete()
    if 'jeden' in results.keys():
        first = Lecture.objects.get( id = results['jeden'])
        l, created = LectureRating.objects.update_or_create(
        user = user, rate =1, defaults = {'lecture': first})
        l.save()
        
    if 'dwa' in results.keys():
        second = Lecture.objects.get(id = results['dwa'])
        l, created = LectureRating.objects.update_or_create(
        user = user, rate = 2, defaults = {'lecture': second})
        l.save()

    if 'trzy' in results.keys():
        third = Lecture.objects.get(id = results['trzy'])
        l, created = LectureRating.objects.update_or_create(
        user = user, rate = 3, defaults = {'lecture': third})
        l.save()

def edit_poll(request):
    if (request.method == 'POST'):
        poll(request.POST, request.user)
        return redirect('/poll/view_poll')
    else:
        ratings = list(LectureRating.objects.filter(user = request.user).order_by('-rate'))
        rate_tuples = [(x.lecture, x.rate,  list(Author.objects.filter(lecture_id = x.lecture))) for x in ratings]
        rated = [x.lecture for x in ratings]
        lecture_list = Lecture.objects.all()
        return render(request, 'poll/view_poll.html', {'lectures': lecture_list, 'ratings': rate_tuples, 'rated': rated}, )

def poll_posters(results, user):
    first = '' 
    second = ''
    third = ''
    PosterRating.objects.filter(user = user).delete()
    if 'jeden' in results.keys():
        first = Poster.objects.get( id = results['jeden'])
        l, created = PosterRating.objects.update_or_create(
        user = user, rate =1, defaults = {'poster': first})
        l.save()
        
    if 'dwa' in results.keys():
        second = Poster.objects.get(id = results['dwa'])
        l, created = PosterRating.objects.update_or_create(
        user = user, rate = 2, defaults = {'poster': second})
        l.save()

    if 'trzy' in results.keys():
        third = Poster.objects.get(id = results['trzy'])
        l, created = PosterRating.objects.update_or_create(
        user = user, rate = 3, defaults = {'poster': third})
        l.save()

def edit_poll_poster(request):
    if (request.method == 'POST'):
        poll_posters(request.POST, request.user)
        return redirect('/poll/view_poll')
    else:
        ratings = list(PosterRating.objects.filter(user = request.user).order_by('-rate'))
        rate_tuples = [(x.poster, x.rate,  list(Author.objects.filter(poster_id = x.poster))) for x in ratings]
        rated = [x.poster for x in ratings]
        poster_list = Poster.objects.all()
        return render(request, 'poll/view_poll_posters.html', {'posters': poster_list, 'ratings': rate_tuples, 'rated': rated}, )

def finish_poll(request):
    if request.method == 'POST':
       form = StatusForm(request.POST)
       if form.is_valid(): 
           poll_status = form.save(commit = False)
           Status.objects.update_or_create(id = 1, defaults = {'poll_status': poll_status.poll_status})
           print(poll_status.poll_status)
       return redirect('/poll/finish_poll')
    else: 
        stat = Status.objects.get(id = 1)
        form = StatusForm(instance = stat) 
        return render(request, 'poll/finish_poll.html', {'form': form})

def results(request):
    rating = list(LectureRating.objects.values('lecture').annotate(rates = Sum('rate')).order_by('-rates'))
    rat = []
    for a in rating:
         rat.append((Lecture.objects.get(id = a['lecture']), a['rates']))

    rating_poster = list(PosterRating.objects.values('poster').annotate(rates = Sum('rate')).order_by('-rates'))
    rat_pos = []
    for a in rating_poster:
         rat_pos.append((Poster.objects.get(id = a['poster']), a['rates']))
    return render(request, 'poll/results.html', {'ratings': rat, 'pos_ratings': rat_pos})
