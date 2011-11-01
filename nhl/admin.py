__author__ = 'Tom'

from nhl.models import *
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    list_filter = ('conference',)

class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('team',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)