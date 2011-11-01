from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    acronym = models.CharField(max_length=5)
    conference = models.CharField(max_length=255, choices=(("E", "Eastern"), ("W", "Western")))
    seasons_played = models.PositiveIntegerField()
    cup_appearances = models.PositiveIntegerField()
    titles = models.PositiveIntegerField()
    wins = models.PositiveIntegerField()
    ties = models.PositiveIntegerField()
    losses = models.PositiveIntegerField()
    shootout_wins = models.PositiveIntegerField()
    shootout_losses = models.PositiveIntegerField()
    division_finish = models.PositiveIntegerField()
    conference_finish = models.PositiveIntegerField()
    goals_for = models.PositiveIntegerField()
    goals_against = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, choices=(("R", "Right Wing"), ("L", "Left Wing"), ("C", "Center"), ("D", "Defense")))
    team = models.ForeignKey("Team")
    games_played = models.PositiveIntegerField()
    goals = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    plus_minus = models.IntegerField()
    penalty_minutes = models.PositiveIntegerField()
    power_play_goals = models.PositiveIntegerField()
    short_handed_goals = models.PositiveIntegerField()
    game_winning_goals = models.PositiveIntegerField()
    shots = models.PositiveIntegerField()
    shot_percentage = models.FloatField()
    average_time = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

