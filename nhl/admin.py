__author__ = 'Tom'

from django.contrib import admin
from nhl.models import *
from nhl.filters import GameListFilter

class TeamAdmin(admin.ModelAdmin):
    list_filter = ('conference',)

class PlayerAdmin(admin.ModelAdmin):
    list_filter = ('team',)

class GameAdmin(admin.ModelAdmin):
    #list_filter = (GameListFilter,)
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)