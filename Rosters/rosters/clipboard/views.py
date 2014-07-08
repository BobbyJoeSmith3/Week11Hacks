from django.shortcuts import render, get_object_or_404
#Import the clipboard app's models
from clipboard.models import Coach, Team, Athlete
# Create your views here.



#This is the page that displays all the teams as links
def teams(request):
	all_teams = Team.objects.all()		#Call all of the teams from the database
	return render(request, 'show_allteams.html', {'all_teams': all_teams})		#Render the data to a template

#This is the page that displays all of the coaches as links
def coaches(request):
	all_coaches = Coach.objects.all()	#Call all of the coaches from the database
	return render(request, 'show_allcoaches.html', {'all_coaches': all_coaches})	#Render the data to a template

#This is the page that displays all of the athletes
def athletes(request):
	all_athletes = Athlete.objects.all()	#Call all of the athletes from the database
	return render(request, 'show_allathletes.html', {'all_athletes': all_athletes})	#Reder the data to a template

#This is the view for a selected team
def teamView(request, team_id_id):
	a_team = get_object_or_404(Team, pk=team_id_id)
	return render(request, 'teamView.html', {'a_team':a_team})