from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from accomodation.forms import AccomodationForm, DinnerForm

class AccomodationView(TemplateView):
    template_name = 'accomodation/edit_accomodation.html'

    def get(self, request):
        form = DinnerForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DinnerForm(request.POST)
        text = ''
        if form.is_valid():
            remark = form.save(commit = False)
            remark.user = request.user
            remark.save() 
            text = form.cleaned_data['remark']
            form = DinnerForm()
            redirect('accomodation:accomodation')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
