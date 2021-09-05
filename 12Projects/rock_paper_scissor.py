import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])#random.choice
    if user == computer:
        return 'tie'

#r > s, s > p, p > r
    if is_win(user, computer):
        return 'You Won!'
    return 'You Lost!'

def is_win(player, opponent):
    #return if player wins
    if (player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r'):
        return True
print(play())