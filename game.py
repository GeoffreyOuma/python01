import random

choices = ["Rock", "Paper", "Scissors"]

def choice():
    selection = random.choice(choices)
    return selection

def winner(playerA, playerB):
    if playerA == "Rock" and playerB == "Rock":
        result = "Tie"
    elif playerA == "Rock" and playerB == "Paper":
        result = "Player B wins"
    elif playerA == "Rock" and playerB == "Scissors":
        result = "Player A wins"
    elif playerA == "Paper" and playerB == "Paper":
        result = "Tie"
    elif playerA == "Paper" and playerB == "Rock":
        result = "Player A wins"
    elif playerA == "Paper" and playerB == "Scissors":
        result = "Player B wins"
    elif playerA == "Scissors" and playerB == "Scissors":
        result = "Tie"
    elif playerA == "Scissors" and playerB == "Rock":
        result = "Player B wins"
    elif playerA == "Scissors" and playerB == "Paper":
        result = "Player A wins"
    return result

player_A_wins = 0
player_B_wins = 0

while player_A_wins != 2 and player_B_wins != 2:
    player_A = choice()
    player_B = choice()
    winr = winner(player_A, player_B)
    print("Player A plays %s" % player_A)
    print("Player B plays %s" % player_B) 
    print(winr)
    # Here's where we'll overwrite the counts of the wins to determine best two of three
    if winr == "Player A wins":
        player_A_wins = player_A_wins + 1
        print("Player A total wins: %i" % player_A_wins)
    elif winr == "Player 2 wins":
        player_B_wins = player_B_wins + 1 
        print("Player B total wins: %i" % player_B_wins)
    else:
        pass
