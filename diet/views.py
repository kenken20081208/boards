from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Meal


def index(request):
    all_meal = Meal.objects.all()
    total = 0
    for meal in all_meal:
        total = total + meal.kcal

    context = {"all_meal": all_meal, "total": total}
    return render(request, "diet/input.html", context)


def create(request):
    name = request.POST.get("name")
    kcal = request.POST.get("kcal")
    new_meal = Meal(name=name, kcal=kcal)
    new_meal.save()
    return HttpResponseRedirect(reverse("diet:index"))


def sum(request):
    context = {}
    return render(request, "diet/input.html", context)
