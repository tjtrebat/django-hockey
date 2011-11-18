from django.shortcuts import *
from django.db.models import Q
from nhl.models import *

def roster(request, team_id, template="nhl/roster.html"):
    return render(request, template, {"players": get_list_or_404(Player, pk=team_id)})

def schedule(request, team_id, template="nhl/schedule.html"):
    return render(request, template, {"games": get_list_or_404(Game, Q(home=team_id) | Q(visitor=team_id))})