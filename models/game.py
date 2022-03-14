def play_game(player1, player2): 

    winner = None 

    if player1.choice == "rock" and player2.choice == "scissors":
        winner = player1 
    elif player1.choice == "scissors" and player2.choice == "paper":
        winner = player1
    elif player1.choice == "paper" and player2.choice == "rock":
        winner = player1
    elif player2.choice == "rock" and player1.choice == "scissors":
        winner = player2
    elif player2.choice == "scissors" and player1.choice == "paper":
        winner = player2
    elif player2.choice == "paper" and player1.choice == "rock":
        winner = player2
    
    return winner 
    
    