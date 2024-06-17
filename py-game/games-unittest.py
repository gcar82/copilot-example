import unittest
from games import get_winner


class TestGame(unittest.TestCase):
    def test_rock_rock(self):
        self.assertEqual(get_winner('rock', 'rock'), "It's a tie!")

    def test_rock_paper(self):
        self.assertEqual(get_winner('rock', 'paper'), "You lose!")

    def test_rock_scissors(self):
        self.assertEqual(get_winner('rock', 'scissors'), "You win!")

    def test_paper_paper(self):
        self.assertEqual(get_winner('paper', 'paper'), "It's a tie!")

    def test_paper_rock(self):
        self.assertEqual(get_winner('paper', 'rock'), "You win!")

    def test_paper_scissors(self):
        self.assertEqual(get_winner('paper', 'scissors'), "You lose!")

    def test_scissors_scissors(self):
        self.assertEqual(get_winner('scissors', 'scissors'), "It's a tie!")

    def test_scissors_rock(self):
        self.assertEqual(get_winner('scissors', 'rock'), "You lose!")

    def test_scissors_paper(self):
        self.assertEqual(get_winner('scissors', 'paper'), "You win!")

if __name__ == '__main__':
    unittest.main()