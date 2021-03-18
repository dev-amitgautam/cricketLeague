from django.shortcuts import render
from json import dumps
from .models import TeamName
import random

# Create your views here.
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def index(request):
    team_names_qualified =[_['team_name'] for _ in TeamName.objects.values('team_name').filter(last_year_qualified = True)]
    team_names_not_qualified =[_['team_name'] for _ in TeamName.objects.values('team_name').filter(last_year_qualified = False)]
    context = dict()
    if team_names_qualified and team_names_not_qualified:
        random.shuffle(team_names_not_qualified)
        team_groups = list(chunks(team_names_not_qualified, 3))
        group_names = ["GROUP A", "GROUP B", "GROUP C", "GROUP D", "GROUP E", "GROUP F", "GROUP G", "GROUP H"]
        groups = dict()
        for i in range(len(group_names)):
            team_groups[i].append(team_names_qualified[i])
            groups[group_names[i]] = team_groups[i]
        context = {"groups": dumps(groups)}

    return render(request, 'cricketGroups/index.html', context)
