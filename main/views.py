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
            "services": Service.objects.all(),
        },
    )


def news(request: HttpRequest):
    return render(
        request,
        "views/news.html",
        {
            "news": New.objects.all().order_by("-posted_at"),
            "services": Service.objects.all(),
            "terminals": Terminal.objects.all(),
        },
    )


def new(request: HttpRequest, new_pk: int):
    return render(
        request,
        "views/new.html",
        {
            "new": New.objects.get(pk=new_pk),
            "terminals": Terminal.objects.all(),
            "services": Service.objects.all(),
        },
    )


def terminal(request: HttpRequest, terminal_pk: int):
    return render(
        request,
        "views/terminal.html",
        {
            "terminal": Terminal.objects.get(pk=terminal_pk),
            "terminals": Terminal.objects.all(),
            "services": Service.objects.all(),
        },
    )


def service(request: HttpRequest, service_pk: int):
    return render(
        request,
        "views/service.html",
        {
            "service": Service.objects.get(pk=service_pk),
            "terminals": Terminal.objects.all(),
            "services": Service.objects.all(),
        },
    )
