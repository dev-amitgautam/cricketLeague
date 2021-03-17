from django.shortcuts import render
from .models import TeamName

# Create your views here.

def index(request):
    team_name = TeamName.objects.all()
    context = {"team_name":team_name}
    return render(request, 'cricketGroups/index.html', context)
