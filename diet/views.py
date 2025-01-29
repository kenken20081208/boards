from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Meal


def index(request):
    all_meal = Meal.objects.all()
    total = 0
    for meal in all_meal:
        total = total + meal.kcal
    if total > 2500:
        warning_message = "警告: これ以上食べたら太るぞ❤️"
    elif total > 4000:
        warning_message = "これ以上はまずいですよ"
    else:
        warning_message = None
    context = {"all_meal": all_meal, "total": total, "warning_message": warning_message}
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
