from django.shortcuts import render
from activities.models import Lecture, Poster, Status, Author 
from abstract_contest.models import ChoosedLecture, ChoosedPoster
from django.http import FileResponse, Http404
import os, subprocess
from tex_templates.tex_const import PREAMBULE, END,  PDF_OUTPUT

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
            l = ChoosedLecture(lecture = lect)
            l.save()    

    accepted_lectures = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
    uncorrect_lectures = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na poprawę")) 
    choosed = Lecture.objects.filter(choosedlecture__in = ChoosedLecture.objects.all())
    args = {'correct_lectures': accepted_lectures, 'uncorrect_lectures': uncorrect_lectures, 'choosed': choosed }
    return render(request, 'abstract_contest/view_lectures.html', args)

@group_required('admins','Komisja')
def choose_posters(request):
    if (request.method == "POST"):
        print(request.POST.getlist('correct'))
        ChoosedPoster.objects.all().delete()
        for poster_id in request.POST.getlist('correct'):
            pos = Poster.objects.get(id = poster_id)
            l = ChoosedPoster(poster = pos)
            l.save()    

    accepted_posters = Poster.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
    uncorrect_posters = Poster.objects.filter(status = Status.objects.get(title = "Czeka na poprawę")) 
    choosed = Poster.objects.filter(choosedposter__in = ChoosedPoster.objects.all())
    args = {'correct_posters': accepted_posters, 'uncorrect_posters': uncorrect_posters, 'choosed': choosed }
    return render(request, 'abstract_contest/view_posters.html', args)

def generate_book(request):
    filename = 'broszurka'
    lectures_list = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
    lectures_with_authors = [(lect, list(Author.objects.filter(lecture_id = lect))) for lect in lectures_list ]
    with open(PDF_OUTPUT + filename +'.tex','w+') as f:
        f.write( PREAMBULE + '\n' )
        f.write(r'\section{Referaty}')
        for (lect, auth) in lectures_with_authors:
            f.write(r'\par \textbf{' + lect.title + r'} \newline' + '\n' +
                    r'\textit{'+ ', '.join([str(a) for a in auth])  +r'} \newline' + '\n' +
                    lect.abstract + r'\newline ' + '\n')
#        f.write(END)
    #f.close()
    posters_list = Poster.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
    posters_with_authors = [(pos, list(Author.objects.filter(poster_id = pos))) for pos in posters_list ]
    print(posters_with_authors)
    with open(PDF_OUTPUT + filename +'.tex','a') as f:
#        f.write( PREAMBULE + '\n' )
        f.write(r'\section{Plakaty}')
        for (pos, auth) in posters_with_authors:
            f.write(r'\par \textbf{' + pos.title + r'} \newline' + '\n' +
                    r'\textit{'+ ', '.join([str(a) for a in auth])  +r'} \newline' + '\n' +
                    pos.abstract + r'\newline ' + '\n')
        f.write(END)
 
    cmd = ['pdflatex', '-interaction', 'nonstopmode', PDF_OUTPUT + filename +'.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    print(retcode)
    if not retcode == 0:
        os.unlink(PDF_OUTPUT + filename +'.pdf')
        print(f)
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

    os.unlink(filename +'.aux')
    os.system("mv broszurka.* " + PDF_OUTPUT  )

    try:
        return FileResponse(open(PDF_OUTPUT + filename +'.pdf', 'rb'), content_type='application/pdf')
    except ValueError:
        pass
