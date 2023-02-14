user_option = input('piedra, papel o tijera? => ')
computer_option = 'papel'

if user_option == computer_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra gana a tijera')
        print('Ganaste!')
    else:
        print('papel gana a piedra')
        print('Perdiste!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('papel gana a piedra')
        print('Ganaste!')
    else:
        print('tijera gana a papel')
        print('Perdiste!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('tijera gana a papel')
        print('Ganaste!')
    else:
        print('piedra gana a tijera')
        print('Perdiste!')