from django.shortcuts import render
from .models import Apartment


def apartments_list(request):
    if str(request.method) == "GET":
        apartments = Apartment.objects.filter(deleted=False)
        return render(request, 'apartments/apartments_list.html', {'apartments':apartments})
