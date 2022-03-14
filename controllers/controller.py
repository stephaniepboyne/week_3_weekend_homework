from flask import render_template, request
from app import app 
from models.player import Player 
from models.game import play_game 

@app.route('/game')
def index():
    return render_template('index.html', title='Play')

@app.route('/game', methods=['POST'])
def enter_choice():
    playerOneChoice = request.form['choice1']
    playerTwoChoice = request.form['choice2']
    player1 = Player("Player One", playerOneChoice)
    player2 = Player("Player Two", playerTwoChoice)
 
    winner = play_game(player1, player2)

    return render_template('winner.html', winner=winner)
