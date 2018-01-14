from django.shortcuts import render, redirect
from activities.models import Lecture, Author
from poll.models import LectureRating
# Create your views here.

def view_poll(request):
    ratings = list(LectureRating.objects.filter(user = request.user).order_by('-rate'))
    rate_tuples = [(x.lecture, x.rate,  list(Author.objects.filter(lecture_id = x.lecture))) for x in ratings]
#        print(rate_tuples)
    return render(request, 'poll/poll_summary.html', {'lectures': rate_tuples, 'user': request.user }
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
#    print(first, second, third)
#    print(lecture_list) 

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
