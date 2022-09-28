def rps_function():
    games=0
    human_wins=0
    computer_wins=0
    draw=0
    import random
    human_turn=input(print('whawill you pick: ','Rock? Scissors? Paper?'))
    print('Human chose: ',human_turn,'.')

    choices=('Rock','Scissors','Paper')

    computer_turn=random.randint(0,2)
    computer_turn=choices[computer_turn]
    print('Computer chose: ',computer_turn,'.')

    if human_turn == 'Rock' and computer_turn =='Scissors':
        human_wins=human_wins+1
        print('Human wins!')
    elif computer_turn == 'Rock' and human_turn =='Scissors':
        computer_wins=computer_wins+1
        print('Computer wins!')


    elif human_turn == 'Paper' and computer_turn =='Rock':
        human_wins=human_wins+1
        print('Human wins!')
    elif computer_turn == 'Paper' and human_turn =='Rock':
        computer_wins=computer_wins+1
        print('Computer wins!')

    elif human_turn == 'Scissors' and computer_turn =='Paper':
        human_wins=human_wins+1
        print('Human wins!')
    elif computer_turn == 'Scissors' and human_turn =='Paper':
        computer_wins=computer_wins+1
        print('Computer wins!')

    else:
        draw=draw+1
        print('Draw')
    games=games+1
    Continue=input("Do you want to continue - yes or no ")
    if Continue == "yes":
        rps_function()
    else:
        print("There has been", games," games.")
        print("Human has won ", human_wins,"games")
        print("but computer has won ", computer_wins,"games")
        print("and there has been draw", draw,"times.")

rps_function()