from django.shortcuts import *
from nhl.models import Player

def roster(request, team_id, template="nhl/_roster.html"):
    return render(request, template, {"players": get_list_or_404(Player, pk=team_id)})