from django.http import HttpRequest
from django.shortcuts import render

from .models import *


def main(request: HttpRequest):
    return render(
        request,
        "views/main.html",
        {
            "news": New.objects.all().order_by("-posted_at")[:3],
            "terminals": Terminal.objects.all(),
        },
    )


def news(request: HttpRequest):
    return render(
        request,
        "views/news.html",
        {
            "news": New.objects.all().order_by("-posted_at"),
            "terminals": Terminal.objects.all(),
        },
    )


def new(request: HttpRequest, new_pk: int):
    return render(
        request,
        "views/new.html",
        {"new": New.objects.get(pk=new_pk), "terminals": Terminal.objects.all()},
    )
