from _decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect

from MusicShop.models import Artist , Recording
from PersonalPage.models import User_Recording_Sell


@login_required(login_url='/accounts/login')
def home(request):
    template = 'PersonalPage/PersonalPage.html'
    context = {}

    return render(request, template, context)


@login_required(login_url='/accounts/login')
def sell_recording(request):
    template = 'PersonalPage/sell_recording.html'
    context = {}
    if request.method == "POST":
        sell_recording = User_Recording_Sell()

        sell_recording.artist = add_artist(request.POST['Artist'])

        sell_recording.recording = add_recording(request.POST['Recording'])
        sell_recording.description = request.POST['Desc']
        sell_recording.user = request.user

        if request.POST['Price'] != '':
            sell_recording.price = Decimal(request.POST['Price'].replace(',',''))
        else:
            sell_recording.price = 0

        sell_recording.save()

        return redirect('correct_add')

    return render(request, template, context)

def add_recording(recording_title):
    try:

        recording = Recording.objects.get(title__exact=recording_title)

    except Recording.DoesNotExist:
        recording = Recording()

        recording.title = recording_title
        recording.artist = None #To implement
        recording.disambiguation = 'To implement'
        recording.release = None # To implement

        recording.save()

    return recording

def add_artist(artist_name):
    try:
        artist = Artist.objects.get(name__exact=artist_name)

    except Artist.DoesNotExist:
        artist = Artist()

        artist.name = artist_name
        artist.country = 'To implement'
        artist.disambiguation = 'To implement'
        artist.type = 'To implement'

        artist.save()

    return artist



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

