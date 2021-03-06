from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm, EditAddProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')  
        else: 
            form = RegistrationForm(request.POST)
            args = {'form': form}
            return render(request, 'accounts/reg_form.html', args)

    else:
        form = RegistrationForm()
        err =  "Wprowadź poprawne dane"
        args = {'form': form, 'err': err}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args) 

def edit_profile(request):
    if request.method =='POST':
        user_form  = EditProfileForm(request.POST, instance = request.user)
        profile_form = EditAddProfileForm(request.POST, instance = request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('accounts:view_profile'))
    
    else:
        user_form = EditProfileForm(instance = request.user)
        profile_form = EditAddProfileForm(instance = request.user.userprofile)
        args = { 
                'user_form': user_form,
                'profile_form': profile_form
                }
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method =='POST':
        form  = PasswordChangeForm(data =request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('view_profile'))
        else:
            return redirect(reverse('change_password'))
    
    else:
        form = PasswordChangeForm( user = request.user)
        args = { 
                'form': form,
                }
        return render(request, 'accounts/change_password.html', args)
