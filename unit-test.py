import random

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

#Generate random numbers for player 1
list1 = generate_random_numbers()
print(list1)
sum1 = calculate_sum(list1)
print(sum1)

#Get user inputs for player 2
list2 = get_user_inputs()
print(list2)
sum2 = calculate_sum(list2)
print(sum2)

#Determine the winner
winner = determine_winner(sum1, sum2)
print(winner)
