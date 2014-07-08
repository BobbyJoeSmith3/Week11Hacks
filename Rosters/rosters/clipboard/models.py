#App: Rosters
#Doc: models.py

from django.db import models

class Team(models.Model):
	team_name = models.CharField(max_length = 100)
	mascot = models.CharField(max_length = 100)

	#Allow us to read the data entries
	def __unicode__(self):
		return self.team_name

class Coach(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	position = models.CharField(max_length = 100)
	team_id = models.ForeignKey(Team)

	#Allow us to read the data entries
	def __unicode__(self):
		return self.first_name

class Athlete(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	position = models.CharField(max_length = 100)
	number = models.CharField(max_length = 2)
	coach_id = models.ManyToManyField(Coach)
	team_id = models.ForeignKey(Team)
	
	#Allow us to read the data entries
	def __unicode__(self):
		return self.first_name