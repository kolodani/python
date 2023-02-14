import random

def choose_option():
    options = ('piedra', 'papel', 'tijera')

    user_option = input('piedra, papel o tijera? => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opcion no es valida')
        return None, None

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('Ganaste!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Perdiste!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('Ganaste!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('Perdiste!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Ganaste!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Perdiste!')
            computer_wins += 1
    return user_wins, computer_wins

def winner(user_wins, computer_wins):
    if user_wins == 2:
        print('Ganaste el juego!')
    elif computer_wins == 2:
        print('Perdiste el juego!')

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while computer_wins < 2 and user_wins < 2:

        print('*' * 10)
        print('RONDA', rounds)
        print('*' * 10)

        print('computadora =>', computer_wins)
        print('usuario =>', user_wins)

        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        winner(user_wins, computer_wins)
        rounds += 1

run_game()