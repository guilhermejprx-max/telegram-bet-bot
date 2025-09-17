import pandas as pd
import numpy as np
from scipy.stats import poisson

# --------------------------
# Sistema de Elo para times
# --------------------------
def calculate_elo(matches, base_elo=1500, k=20):
    teams = {}
    for _, row in matches.iterrows():
        home, away = row['home_team'], row['away_team']
        hg, ag = row['home_goals'], row['away_goals']

        if home not in teams:
            teams[home] = base_elo
        if away not in teams:
            teams[away] =
