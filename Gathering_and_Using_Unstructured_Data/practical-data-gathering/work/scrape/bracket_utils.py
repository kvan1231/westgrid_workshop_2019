import numpy as np

def series(pmat,i,j):
    wins = [0,0]
    while wins[0] < 4 and wins[1] < 4:
        won = np.random.binomial(1,pmat[i][j])
        if won:
            wins[0] += 1
        else:
            wins[1] += 1
            
    if wins[0] == 4:
        winner = i
    if wins[1] == 4:
        winner = j
    return winner, sum(wins)

def trial(pmat):
    assert pmat.shape[0] == pmat.shape[1], 'non square p matrix!'
    
    N = pmat.shape[0]
    
    indicies = list(range(0,N))
    
    games_played = np.zeros((N,))

    temp = []
    
    while len(indicies) > 1:
        
        i = indicies.pop(0)
        j = indicies.pop(0)
        
        winner, num_games = series(pmat,i,j)
        
        games_played[i] += num_games
        games_played[j] += num_games
        
        indicies.append(winner)
    
    return indicies[0],games_played

def trial_with_rounds(pmat):
    assert pmat.shape[0] == pmat.shape[1], 'non square p matrix!'
    
    N = pmat.shape[0]
    
    indicies = list(range(0,N))
    
    games_played = np.zeros((N,))

    temp = []
    
    M = int(np.log2(N)) + 1
    rounds = -1*np.ones((N,M))
    
    round_count = 0
    rounds[:,round_count] = indicies
    round_count += 1 
    
    while len(indicies) > 1:
        
        i = indicies.pop(0)
        j = indicies.pop(0)
        
        winner, num_games = series(pmat,i,j)
        
        games_played[i] += num_games
        games_played[j] += num_games
        
        indicies.append(winner)
            
        if len(indicies) == N//2:
            
            diff = pmat.shape[0] - len(indicies)
            rounds[:,round_count] = indicies + [-1]*diff
            N = len(indicies)
            round_count += 1
    
    return indicies[0],games_played,rounds


def simulate(N,pmat,include_rounds=False):
    rounds = []
    winners = []
    
    M = pmat.shape[0]
    total_games_played = np.zeros((N,M))
    
    for i in range(0,N):
        if include_rounds:
            winner,games_played,rnd = trial_with_rounds(pmat)
            rounds.append(rnd)
        else:
            winner,games_played = trial(pmat)
        
        winners.append(winner)
        
        total_games_played[i,:] = games_played
    
    return total_games_played,winners,rounds



if __name__ == "__main__":
    np.random.seed(0)

    N = 16
    random = np.random.rand(N,N)
    upper = np.triu(random,k=1)
    lower = np.tril(1- np.transpose(upper),k=-1)
    pmat = upper + lower
    print(pmat)


    TGP = simulate(100000,pmat)
    
    AGP = np.mean(TGP,axis=0)

    print(AGP)
