from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import nbashots as nba


# Create your views here.
def index(request):
  curry_id = nba.get_player_id("Curry, Stephen")[0]
  print(curry_id)
  curry_shots_df = nba.Shots(curry_id).get_shots()
  plt.rcParams['figure.figsize'] = (12, 11)
  nba.shot_chart(curry_shots_df.LOC_X, curry_shots_df.LOC_Y, kind='hex', gridsize=100,
                title="Stephen Curry FGA 2015-16 Season")

  image = plt.show()
  HttpResponse(render(image))
  