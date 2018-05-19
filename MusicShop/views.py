# Create your views here.
from django.shortcuts import render

from PersonalPage.models import User_Recording_Sell


def home(request):
    template = 'home.html'
    all_sell_recordings = User_Recording_Sell.objects.all()

    return render(request, template, {'all_sell_recodings': all_sell_recordings})
