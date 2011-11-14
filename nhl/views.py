from django.http import Http404
from django.shortcuts import *
from nhl.models import Player

def roster(request, team, template="nhl/_roster.html"):
    if request.is_ajax():
        return render(request, template, {"players": get_list_or_404(Player, team__acronym__iexact=team)})
    raise Http404