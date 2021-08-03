import random

def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors \nUser Choice:")
    computer = random.choice(['r', 'p', 's'])
    print("Computer Choice "+computer)

    if user == computer:
        return "It's a Tie"
    
    if is_win(user, computer):
        return "You Won"
    return "Computer Won"

def is_win(player, opponents):
    # return true if player win
    # r > s, s > p, p > r
    if(player == 'r' and opponents == 's') or (player == 's' and opponents == 'p') or (player == 'p' and opponents == 'r'):
        return True
print(play())