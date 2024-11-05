from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ["title", "pk", "content", "posted_at"]
    readonly_fields = ("posted_at",)


@admin.register(Terminal)
class TerminalAdmin(admin.ModelAdmin):
    list_display = ["name", "pk"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "pk"]
