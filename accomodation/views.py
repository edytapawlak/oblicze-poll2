from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accomodation.forms import AccomodationForm, DinnerForm 
from accomodation.models import Dinner, Hostel

class AccomodationView(TemplateView):
    template_name = 'accomodation/edit_accomodation.html'
    def get(self, request):
         # Do zmiany na jakiś mądrzejszy sposób 
        dinner_days_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ] 
        hostel_dates_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ]

        user = request.user
        
        dinners = Dinner.objects.filter(user = user)
        checked_din = [str(x.date) for x in dinners]
        checked_vege = [str(x.date) for x in dinners if x.vege]
        remark = ''
        for dinner in dinners:
            remark += dinner.remark + ' '

        form_dinner = DinnerForm(initial = {'remark': remark})

        nights = Hostel.objects.filter(user = user)
        checked_night = [str(x.date) for x in nights]
        print(checked_night)

        form_accomodation = AccomodationForm()
        args =  {'form_dinner': form_dinner, 'form_accomodation': form_accomodation, 'dinner_dates' : dinner_days_list, 'hostel_dates': hostel_dates_list, 'user_din': checked_din, 'user_vege': checked_vege, 'user_nights': checked_night, }

        for dinner in request.GET.getlist('date'): 
            print(dinner)
       
        return render(request, self.template_name, args)

    def post(self, request):
        # Do zmiany na jakiś mądrzejszy sposób 
        dinner_days_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ] 
        hostel_dates_list = [ '2011-11-11', '2011-11-12', '2011-11-13' ]

        if request.method == 'POST':
            form = DinnerForm(request.POST)
            text = ''
            
            if form.is_valid():
                dates =request.POST.getlist('date') 
                vegeDinner = request.POST.getlist('isVege')
                for dinner_date in dinner_days_list:
                    if dinner_date in dates:
                        update_value = {}               
                        update_value['remark'] = form.cleaned_data['remark']
                        if (dinner_date in vegeDinner):
                            update_value['vege'] = True
                        else: 
                            update_value['vege'] = False
                        remark, created = Dinner.objects.update_or_create(user = request.user, date = dinner_date, defaults = update_value)
                    else:
                        try:
                            Dinner.objects.get(user = request.user, date = dinner_date).delete()
                        except Dinner.DoesNotExist:
                            pass

                hostel_nights = request.POST.getlist('hostel_date')
                for night in hostel_dates_list:
                    if (night in hostel_nights):
                        accomo, created = Hostel.objects.update_or_create(user = request.user, date = night)                
                    else:
                        try:
                            n = Hostel.objects.get(user = request.user, date = night).delete()
                        except Hostel.DoesNotExist:
                            pass
                            
                form_dinner = DinnerForm()
                form_accomodation = AccomodationForm()
            redirect('accomodation:accomodation')
            args = {'form_dinner': form_dinner, 'form_accomodation': form_accomodation, 'dinner_dates' : dinner_days_list, 'hostel_dates': hostel_dates_list }
  
        return render(request, self.template_name, args)
