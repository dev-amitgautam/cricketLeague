from django.db import models


# Create your models here.

class TeamName(models.Model):
    team_name = models.CharField(primary_key=True ,max_length=200)
    state = models.CharField(max_length=100)
    last_year_qualified = models.BooleanField(default=False)

    def __str__(self):
        return self.team_name

    class Meta:
        db_table = "all_teams"
