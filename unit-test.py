import random
import unittest

def generate_random_numbers():
    return [random.randrange(21) for _ in range(5)]

def get_user_inputs():
    return [int(input('Enter number: ')) for _ in range(5)]

def calculate_sum(numbers):
    return sum(numbers)

def determine_winner(sum1, sum2):
    if sum1 > sum2:
        return 'Player 1 is the winner'
    else:
        return 'Player 2 is the winner'

class MyTestCase(unittest.TestCase):
    def test_game(self):
        # Generate random numbers for player 1
        list1 = generate_random_numbers()
        self.assertEqual(len(list1), 5)
        sum1 = calculate_sum(list1)
        self.assertEqual(sum1, sum(list1))

        # Get user inputs for player 2
        list2 = get_user_inputs()
        self.assertEqual(len(list2), 5)
        sum2 = calculate_sum(list2)
        self.assertEqual(sum2, sum(list2))

        # Determine the winner
        winner = determine_winner(sum1, sum2)
        self.assertIn(winner, ['Player 1 is the winner', 'Player 2 is the winner'])

if __name__ == '__main__':
    unittest.main()
