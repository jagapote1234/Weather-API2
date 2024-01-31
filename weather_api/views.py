from django.shortcuts import render
from .forms import CityForm

import requests
import json

# Create your views here.


def IndexView(request):
    if request.method == 'POST':
        form = CityForm   
        context = {
            'form': form,
        }

    return render(request, 'weather/index.html', context)


