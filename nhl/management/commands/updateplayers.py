__author__ = 'Tom'

import urllib2
from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from hockey.nhl.models import *

class Command(BaseCommand):
    args = '<team_acronym team_acronym ...>'
    help = 'Updates players with specified Team abbreviation'

    def handle(self, *args, **options):
        team_acronyms = list(args)
        if not len(team_acronyms):
            for team in Team.objects.all():
                team_acronyms.append(team.acronym)
        for team_acronym in team_acronyms:
            try:
                team = Team.objects.get(acronym=team_acronym)
            except Team.DoesNotExist:
                raise CommandError('Team "%s" does not exist' % team_acronym)

            soup = BeautifulSoup(urllib2.urlopen("http://www.nhl.com/ice/playerstats.htm?season=20112012&team=" + team_acronym).read())

            for row in soup('table', {'class' : 'data stats'})[0].tbody('tr'):
                tds = row('td')
                player_name = tds[1]('a')[0].string
                try:
                    player = Player.objects.get(name=player_name, team=team)
                except Player.DoesNotExist:
                    player = Player(name=player_name, team=team)
                player.position = tds[3].string
                player.games_played = tds[4].string
                player.goals = tds[5].string
                player.assists = tds[6].string
                player.points = tds[7].string
                player.plus_minus = tds[8].string
                player.penalty_minutes = tds[9].string
                player.power_play_goals = tds[10].string
                player.short_handed_goals = tds[11].string
                player.game_winning_goals = tds[12].string
                player.shots = tds[14].string
                player.shot_percentage = tds[15].string
                player.average_time = tds[16].string
                player.save()

            self.stdout.write('Successfully updated "%s"\n' % team)