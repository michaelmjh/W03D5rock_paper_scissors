import random
from models.game import Game
from models.player import Player

current_game = []
winner = None

def clear_current_game():
    current_game.clear()
    winner = None
    single_player_game = None

def add_player_to_game(player):
    current_game.append(player)

def generate_computer_player():
    shape = generate_random_shape()
    new_player = Player("Computer", shape)
    add_player_to_game(new_player)

def generate_random_shape():
    index = random.randint(0,2)
    if index == 0:
        return "Rock"
    elif index == 1:
        return "Paper"
    elif index == 2:
        return "Scissors"

def generate_winner():
    new_game = Game(current_game[0], current_game[1])
    return new_game.play_game()




