# coding=utf-8

from django.contrib import admin
from .models import SiteMail, Notification, Task


@admin.register(SiteMail)
class SiteMailAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
