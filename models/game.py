class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.shape == "Rock":
            if self.player_2.shape == "Scissors":
                return self.player_1
            elif self.player_2.shape == "Paper":
                return self.player_2
        elif self.player_1.shape == "Paper":
            if self.player_2.shape == "Rock":
                return self.player_1
            elif self.player_2.shape == "Scissors":
                return self.player_2
        elif self.player_1.shape == "Scissors":
            if self.player_2.shape == "Paper":
                return self.player_1
            elif self.player_2.shape == "Rock":
                return self.player_2
        else:
            return None

    def play_basic(shape_1, shape_2):
        if shape_1 == "Rock":
            if shape_2 == "Scissors":
                return f"Player 1 wins by playing {shape_1}"
            elif shape_2 == "Paper":
                return f"Player 2 wins by playing {shape_2}"
        elif shape_1 == "Paper":
            if shape_2 == "Rock":
                return f"Player 1 wins by playing {shape_1}"
            elif shape_2 == "Scissors":
                return f"Player 2 wins by playing {shape_2}"
        elif shape_1 == "Scissors":
            if shape_2 == "Paper":
                return f"Player 1 wins by playing {shape_1}"
            elif shape_2 == "Rock":
                return f"Player 2 wins by playing {shape_2}"
        else:
            return None