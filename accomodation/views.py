from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accomodation.forms import AccomodationForm, DinnerForm, ALL_DATES

class AccomodationView(TemplateView):
    template_name = 'accomodation/edit_accomodation.html'

    def get(self, request):
        form_dinner = DinnerForm()
        form_accomodation =None # AccomodationForm()
        days_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ] 

        args =  {'form_dinner': form_dinner, 'form_accomodation': form_accomodation, 'dates' : days_list }
        return render(request, self.template_name, args)

    def post(self, request):
        if request.method == 'POST':
            form = DinnerForm(request.POST)
            text = ''
            print(dict(ALL_DATES))
            
            if form.is_valid():
                dates =request.POST.getlist('dates') 
                for date in dates:
                    remark = form.save(commit = False)
                    remark.date= date 
                    remark.pk = None
                    remark.user = request.user
                    remark.save() 

                form = DinnerForm()
                redirect('accomodation:accomodation')
                days_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ] 

        args = {'form_dinner': form, 'dates': days_list }
        return render(request, self.template_name, args)
