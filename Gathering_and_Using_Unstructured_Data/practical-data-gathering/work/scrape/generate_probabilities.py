import pandas as pd
import numpy as np

import json

def check_symmetric(a, tol=1e-8):
    return np.allclose(a, a.T, atol=tol)

def gen_prob(bracket,season_dataframes):
    
    teams = bracket['first_round']
    
    dataframes = []
    df = pd.concat(season_dataframes)
    
    filtered = df[df['visitor_team_name'].isin(teams)&df['home_team_name'].isin(teams)]
    
    N = len(teams)
    wins = np.zeros((N,N))

    for row in filtered.iterrows():
        data = row[1]
        h = data.home_team_name
        v = data.visitor_team_name
        gh = data.home_goals
        gv = data.visitor_goals

        if gh > gv:
            i = teams.index(h)
            j = teams.index(v)
            wins[i][j] += 1
        elif gv > gh:
            i = teams.index(v)
            j = teams.index(h)
            wins[i][j] += 1
        else:
            print(f'error in game on {data.date_game}, with notes: {data.game_remarks}')
            
    print(f"symmetric wins matrix: {check_symmetric(np.transpose(wins)+wins)}")
    
    pmat = np.nan_to_num((wins+1)/(wins.T+wins + 2))
    
    return pmat
