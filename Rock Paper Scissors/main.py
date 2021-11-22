import random


def play():
    user = input("'r' for rock,'p' for paper,'s' for scissors ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'tie'
    if isWin(user, computer):
        return 'You won'
    print("computer had "+computer)
    return 'you lost'


def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        print("opponent had a "+opponent)
        return True


print(play())
