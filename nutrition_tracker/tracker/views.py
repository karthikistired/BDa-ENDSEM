# views.py

from django.shortcuts import render
from .models import FoodIntake

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        fats = float(request.POST['fats'])
        carbs = float(request.POST['carbs'])
        protein = float(request.POST['protein'])
        FoodIntake.objects.create(name=name, fats=fats, carbs=carbs, protein=protein)
        return render(request, 'tracker/home.html', {'calories': (fats * 9) + (carbs * 4) + (protein * 4)})
    return render(request, 'tracker/home.html')

def intake_details(request):
    intakes = FoodIntake.objects.all()
    return render(request, 'tracker/intake_details.html', {'intakes': intakes})
