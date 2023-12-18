import random

# print('Rock, Paper, Scissors Game')

options = ["rock", 'paper', 'scissors']

while True:
    user_choice = input("rock, paper, scissors? ")

    while user_choice not in options:
        user_choice = input("rock, paper, scissors? ").lower()

    random_num = random.randint(0, 2)
    print(random_num)

    def find_winner(computer, user):
        awnsers = "{0}{1}".format(options[computer], user)
        if (awnsers == "rockpaper" or 
            awnsers == "paperscissors" or 
            awnsers == "scissorsrock"):
            print("congrats you win")
        elif options[computer] == user:
            print('draw')
        else:
            print('you lose')

        print('computer: '+ options[computer])
        print('user: '+ user)

    find_winner(random_num, user_choice)

    should_play_again = input("type (y) to Play Again or anykey to quit ").lower()
    if should_play_again != 'y':
        break
