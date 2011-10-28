__author__ = 'Tom'

from nhl.models import *
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_filter = ('conference',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Player)