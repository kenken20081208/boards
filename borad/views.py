from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from borad import models


def pepe(request):
    moji = request.POST.get("moji")
    new_moji = models.Borad(moji=moji)
    new_moji.save()

    return HttpResponseRedirect(reverse("borad:index"))


def index(request):
    all_moji = models.Borad.objects.all()
    context = {"all_moji": all_moji}
    return render(request, "borad/index.html", context)
