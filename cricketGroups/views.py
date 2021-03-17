from django.shortcuts import render
from .models import TeamName
import random

# Create your views here.
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def index(request):
    team_names_qualified = list(TeamName.objects.filter(last_year_qualified = True))
    team_names_not_qualified = list(TeamName.objects.filter(last_year_qualified = False))
    random.shuffle(team_names_not_qualified)
    team_groups = list(chunks(team_names_not_qualified, 3))
    group_names = ["GROUP A", "GROUP B", "GROUP C", "GROUP D", "GROUP E", "GROUP F", "GROUP G", "GROUP H"]
    groups = dict()
    for i in range(8):
        team_groups[i].append(team_names_qualified[i])
        groups[group_names[i]] = team_groups[i]

    context = {"groups": groups}
    return render(request, 'cricketGroups/index.html', context)
