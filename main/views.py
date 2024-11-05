from django.http import HttpRequest
from django.shortcuts import render

from .models import New


def main(request: HttpRequest):
    return render(
        request,
        "views/main.html",
        {"news": New.objects.all().order_by("-posted_at")[:3]},
    )


def news(request: HttpRequest):
    return render(
        request,
        "views/news.html",
        {"news": New.objects.all().order_by("-posted_at")},
    )
