class Game:

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def play_game(self):
        if self.player_1.shape == "rock":
            if self.player_2.shape == "scissors":
                return self.player_1
            elif self.player_2.shape == "paper":
                return self.player_2
        elif self.player_1.shape == "paper":
            if self.player_2.shape == "rock":
                return self.player_1
            elif self.player_2.shape == "scissors":
                return self.player_2
        elif self.player_1.shape == "scissors":
            if self.player_2.shape == "paper":
                return self.player_1
            elif self.player_2.shape == "rock":
                return self.player_2
        else:
            return None
