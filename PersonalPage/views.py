from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/accounts/login')
def home(request):
    template = 'PersonalPage/PersonalPage.html'
    context = {}

    return render(request, template, context)


@login_required(login_url='/accounts/login')
def sell_recording(request):
    template = 'PersonalPage/sell_recording.html'
    context = {}

    return render(request, template, context)


@login_required(login_url='/accounts/login')
def edit_recording(request):
    template = 'PersonalPage/edit_recording.html'
    context = {}

    return render(request, template, context)

@login_required(login_url='/accounts/login')
def correct_add(request):
    template = 'PersonalPage/correct_add.html'
    context = {}

    return render(request, template, context)