# https://www.algoexpert.io/questions/tournament-winner
def tournamentWinner(competitions, results):
    # Write your code here.
    winner = {}
    player = ""
    i = 0
    while i < len(competitions):
        if results[i] == 0:
            player = competitions[i][1]
        else:
            player = competitions[i][0]

        if player not in winner:
            winner[player] = 3
        else:
            winner[player] += 3
        i += 1
    winnig_val = -1
    for i in winner:
        if winner[i] > winnig_val:
            winnig_val = winner[i]
            player = i
    return player
