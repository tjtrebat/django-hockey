from django.http import HttpResponse, Http404
from django.core import serializers
from nhl.models import Player

def roster(request, team):
    if request.is_ajax():
        return HttpResponse(serializers.serialize("json", Player.objects.filter(team__acronym__iexact=team)))
    raise Http404