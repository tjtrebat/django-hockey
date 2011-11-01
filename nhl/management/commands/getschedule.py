__author__ = 'Tom'

import urllib2
import datetime
from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
from hockey.nhl.models import *

class Command(BaseCommand):
    args = '<team_acronym team_acronym ...>'
    help = 'Updates players with specified Team abbreviation'

    def handle(self, *args, **options):
        soup = BeautifulSoup(urllib2.urlopen("http://www.nhl.com/schedules/20112012.html").read())
        for row in soup('table', {'class' : 'data schedTbl'})[0].tbody('tr'):
            tds = row('td')
            date = tds[0]('div')
            if len(date) > 0:
                time = tds[3]('div')[0].string.split()
                time = " ".join(time[0:2])
                try:
                    visitor = Team.objects.get(acronym=self.get_rel_attr(tds[1]('div', {'class': 'teamName'})[0]('a')[0]))
                    home = Team.objects.get(acronym=self.get_rel_attr(tds[2]('div', {'class': 'teamName'})[0]('a')[0]))
                except Team.DoesNotExist:
                    pass
                else:
                    game, created = Game.objects.get_or_create(visitor=visitor,
                                                               home=home,
                                                               time=datetime.datetime.strptime("%s %s" % (date[0].string, time),
                                                                                               "%a %b %d, %Y %I:%M %p"))
                    self.stdout.write('Successfully added "%s"\n' % game)

    def get_rel_attr(self, tag):
        rel_attr = ""
        for attr in tag.attrs:
            if attr[0] == "rel":
                rel_attr = attr[1]
        return rel_attr
