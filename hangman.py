#####  Hangman Benedict Laiman  #####

import random

def hangman():
    hangman = ["""
    _____
    """, """
    _____
    |   |
    """, """
    _____
    |   |
    |   o
    """, """
    _____
    |   |
    |   o
    |  /|\\
    """, """
    _____
    |   |
    |   o
    |  /|\\
    |  / \\

    """, """
    _____
    |   |
    |   o
    |  /|\\
    |  / \\
    |____
    """]

    questions = [
        ['4 letters! Name of a drink that baby consumes', 'milk'],
        ['4 letters! Zebra-like animal', 'horse'],
        ['4 letters! Red-colored fruit', 'apple']
    ]

    logo = ['''
    
 ▄▄▄▄   ▓█████  ███▄    █ ▓█████ ▓█████▄  ██▓ ▄████▄  ▄▄▄█████▓  ██████     ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓█████▄ ▓█   ▀  ██ ▀█   █ ▓█   ▀ ▒██▀ ██▌▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██    ▒    ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▒ ▄██▒███   ▓██  ▀█ ██▒▒███   ░██   █▌▒██▒▒▓█    ▄ ▒ ▓██░ ▒░░ ▓██▄      ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
▒██░█▀  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█▄   ▌░██░▒▓▓▄ ▄██▒░ ▓██▓ ░   ▒   ██▒   ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█  ▀█▓░▒████▒▒██░   ▓██░░▒████▒░▒████▓ ░██░▒ ▓███▀ ░  ▒██▒ ░ ▒██████▒▒   ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
░▒▓███▀▒░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░ ░▒ ▒  ░  ▒ ░░   ▒ ▒▓▒ ▒ ░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
▒░▒   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░  ░  ▒       ░    ░ ░▒  ░ ░    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░    ░    ░      ░   ░ ░    ░    ░ ░  ░  ▒ ░░          ░      ░  ░  ░      ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░         ░  ░         ░    ░  ░   ░     ░  ░ ░                     ░      ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
      ░                           ░          ░                                                                                                  
    ''']

    while True:  # While true loop
        # To randomize the questions
        randomizer = random.randint(0, (len(questions) - 1))
        print(logo[0])
        print(questions[randomizer][0])
        life = 6
        attempt = int()
        placeholder = list('_ ' * len(questions[randomizer][1]))
        while life >= 0:
            if life > 0:
                attempt += 1
                if '_' not in placeholder:  # To check if the player is correct or not (win or lose)
                    break
                answer = input(
                    f'Input 1 character/ letter, attempt {attempt} : ').lower()
                # To check if player input the same letter as the answer or input more than 1 letter
                if (answer == questions[randomizer][1]) or (len(answer) != 1):
                    print('Only one character at a time!')
                    continue
                if answer in questions[randomizer][1]:  # If the player correctly guesses the answer
                    for i in range(len(questions[randomizer][1])):
                        if questions[randomizer][1][i] == answer:
                            del placeholder[2 * i]
                            placeholder.insert(
                                (2 * i), questions[randomizer][1][i])
                    print(''.join(placeholder))
                else:  # If the player wrongly guesses the answer
                    print(''.join(placeholder))
                    life -= 1
                    print(f'You have {life}/6 lifes remaining \n')
                    print(hangman[-(life + 1)])
            elif life == 0:
                break
        if '_' not in placeholder:  # To check if the player wins the game or not
            print('You are correct!')
        else:  # After the loop is break due to zero life
            print('YOU ARE DEAD \n')
        # Ask player to play again
        askuser = input('Do you want to play again? (y/n) : ')
        if askuser == 'y':
            continue
        elif askuser == 'n':
            print('\n Game Over, Starting over... ')
            break
        else:
            print('Please input the right answer! Never mind, we just start over the game :v ')
            continue


hangman()


# ▄▄▄▄   ▓█████  ███▄    █ ▓█████ ▓█████▄  ██▓ ▄████▄  ▄▄▄█████▓  ██████     ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █
# ▓█████▄ ▓█   ▀  ██ ▀█   █ ▓█   ▀ ▒██▀ ██▌▓██▒▒██▀ ▀█  ▓  ██▒ ▓▒▒██    ▒    ▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █
# ▒██▒ ▄██▒███   ▓██  ▀█ ██▒▒███   ░██   █▌▒██▒▒▓█    ▄ ▒ ▓██░ ▒░░ ▓██▄      ▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
# ▒██░█▀  ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ░▓█▄   ▌░██░▒▓▓▄ ▄██▒░ ▓██▓ ░   ▒   ██▒   ░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
# ░▓█  ▀█▓░▒████▒▒██░   ▓██░░▒████▒░▒████▓ ░██░▒ ▓███▀ ░  ▒██▒ ░ ▒██████▒▒   ░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
# ░▒▓███▀▒░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░ ░▒ ▒  ░  ▒ ░░   ▒ ▒▓▒ ▒ ░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒
# ▒░▒   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░  ░  ▒       ░    ░ ░▒  ░ ░    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
# ░    ░    ░      ░   ░ ░    ░    ░ ░  ░  ▒ ░░          ░      ░  ░  ░      ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░
# ░         ░  ░         ░    ░  ░   ░     ░  ░ ░                     ░      ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░
# ░                           ░          ░

# 4 letters! Red-colored fruit
# Input 1 character/ letter, attempt 1 : a
# a _ _ _ _
# Input 1 character/ letter, attempt 2 :