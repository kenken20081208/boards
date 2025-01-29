from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Meal


def index(request):
    all_meal = Meal.objects.all()
    context = {"all_meal": all_meal}
    return render(request, "diet/input.html", context)


def create(request):
    name = request.POST.get("name")
    kcal = request.POST.get("kcal")
    new_meal = Meal(name=name, kcal=kcal)
    new_meal.save()
    return HttpResponseRedirect(reverse("diet:indx"))


def sum(request):
    context = {}
    return render(request, "diet/input.html", context)
