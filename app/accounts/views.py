from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


def signup(request):

    if request.method == "GET":

        return render(request, 'accounts/signup.html', {
            'form': CustomUserCreationForm(),
            'next': request.GET.get('next')
        })

    else: 

        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            new_user = f.save()
            login(request, new_user)
            return HttpResponseRedirect(request.POST.get('next'))

        return render(request, 'accounts/signup.html', {
            'form': f,
            'next': request.POST.get('next')
        })