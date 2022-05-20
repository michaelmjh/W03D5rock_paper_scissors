import unittest
from models.game import Game
from models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player_rock = Player("rock", "rock")
        self.player_paper = Player("paper", "paper")
        self.player_scissors = Player("scissors", "scissors")

        self.game_rock_scissors = Game(self.player_rock, self.player_scissors)
        self.game_rock_paper = Game(self.player_rock, self.player_paper)
        self.game_rock_rock = Game(self.player_rock, self.player_rock)

        self.game_paper_rock = Game(self.player_paper, self.player_rock)
        self.game_paper_scissors = Game(self.player_paper, self.player_scissors)
        self.game_paper_paper = Game(self.player_paper, self.player_paper)

        self.game_scissors_paper = Game(self.player_scissors, self.player_paper)
        self.game_scissors_rock = Game(self.player_scissors, self.player_rock)
        self.game_scissors_scissors = Game(self.player_scissors, self.player_scissors)


    def test_play_game_rock_scissors(self):
        self.assertEqual(self.player_rock, self.game_rock_scissors.play_game())

    def test_play_game_rock_paper(self):
        self.assertEqual(self.player_paper, self.game_rock_paper.play_game())

    def test_play_game_rock_rock(self):
        self.assertIsNone(self.game_rock_rock.play_game())

    def test_play_game_paper_rock(self):
        self.assertEqual(self.player_paper, self.game_paper_rock.play_game())
  
    def test_play_game_paper_scissors(self):
        self.assertEqual(self.player_scissors, self.game_paper_scissors.play_game())

    def test_play_game_paper_paper(self):
        self.assertIsNone(self.game_paper_paper.play_game())

    def test_play_game_scissors_paper(self):
        self.assertEqual(self.player_scissors, self.game_scissors_paper.play_game())

    def test_play_game_scissors_rock(self):
        self.assertEqual(self.player_rock, self.game_scissors_rock.play_game())

    def test_play_game_scissors_scissors(self):
        self.assertIsNone(self.game_scissors_scissors.play_game())