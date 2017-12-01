from django.shortcuts import render
from activities.models import Lecture, Status, Author 
from abstract_contest.models import ChoosedLecture
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

def generate_book(request):
    filename = 'broszurka'
    lectures_list = Lecture.objects.filter(status = Status.objects.get(title = "Czeka na akceptację")) 
 
#    lectures_list = Lecture.objects.all()
    lectures_with_authors = [(lect, Author.objects.get(lecture_id = lect)) for lect in lectures_list ]
    with open(PDF_OUTPUT + filename +'.tex','w+') as f:
        f.write( PREAMBULE + '\n' )
        for (lect, auth) in lectures_with_authors:
            f.write(r'\par \textbf{' + lect.title + r'} \newline' + '\n' +
                    r'\textit{'+ str(auth)  +r'} \newline' + '\n' +
                    lect.abstract + r'\newline ' + '\n')
        f.write(END)
    f.close()

    cmd = ['pdflatex', '-interaction', 'nonstopmode', PDF_OUTPUT + filename +'.tex']
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink(PDF_OUTPUT + filename +'.pdf')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

    os.unlink(filename +'.aux')
    os.system("mv broszurka.* " + PDF_OUTPUT  )

    try:
        return FileResponse(open(PDF_OUTPUT + filename +'.pdf', 'rb'), content_type='application/pdf')
    except ValueError:
        print(Tujestźle)
