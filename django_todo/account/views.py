from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'todo/sign_up.html', {'form': form})
