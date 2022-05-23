from app import app
from flask import render_template, request
from models.current_game import *
from models.player import Player
from models.game import Game
from models.current_game import *

@app.route("/")
def index():
    clear_current_game()
    return render_template("home.html", title="Home")

@app.route("/single_player")
def play_game_single():
    generate_computer_player()
    return render_template("play.html", title="Play Game")

@app.route("/play")
def play_game_multi():
    return render_template("play.html", title="Play Game")

@app.route("/play", methods=['POST'])
def add_player():  
    p_name = request.form['name']
    p_shape = request.form['shape']

    new_player = Player(p_name, p_shape)
    add_player_to_game(new_player)

    if len(current_game) == 1:
        return render_template("play.html", title="Play Game")
    else:
        winner = generate_winner()
        return render_template("result.html", title="Home", players=current_game, winner=winner)

@app.route("/result")
def show_outcome():
    return render_template("result.html", title="result", winner=winner)

@app.route('/<shape_1>/<shape_2>')
def rock_scissors(shape_1, shape_2):
    result = Game.play_basic(shape_1.title(), shape_2.title())
    if result != None:
        return result
    else:
        return "It's a draw"
