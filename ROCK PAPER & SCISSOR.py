import random

i = 1
w = 0
a = 0
t = 0
Wins = ''
Losses = ''
symbol1 = ''
symbol2 = ''
while True:
    if i == 1:
        print("\n\t\t\t\t\t Welcome to ROCK PAPER AND SCISSORS!\n")
    elif i >= 1:
        print(
            f' \t\t\t\t\t Game counter ⏱  = {counter}\n\n\tTotal win(s) 🏆 = {Wins}\t\t  Total Tie(s) = {Ties}\t\t Total loss(es) ☠  = {Losses}\n')

    robot = ""
    comp_turn = random.randint(1, 3)
    if comp_turn == 1:
        robot = 'rock'

    elif comp_turn == 2:
        robot = 'paper'

    elif comp_turn == 3:
        robot = 'scissor'

    your_turn = (input('Enter your choice: ')).lower()

    if robot == 'rock' and your_turn == 'paper':
        print('Congratulations! You win')
        w += 1
        symbol1 = "🎫"
        symbol2 = "🧱"

    elif robot == 'rock' and your_turn == 'scissor':
        print('You lose, better luck next time!')
        a += 1
        symbol2 = "🧱"
        symbol1 = "✂."

    elif robot == 'paper' and your_turn == 'rock':
        print('You lose, better luck next time!')
        a += 1
        symbol1 = "🧱"
        symbol2 = "🎫"

    elif robot == 'paper' and your_turn == 'scissor':
        print('Congratulations! You win')
        w += 1
        symbol2 = "🎫"
        symbol1 = "✂."

    elif robot == 'scissor' and your_turn == 'rock':
        print('Congratulations! You win')
        w += 1
        symbol1 = "🧱"
        symbol2 = "✂."

    elif robot == 'scissor' and your_turn == 'paper':
        print('You lose, better luck next time!')
        a += 1
        symbol1 = "🎫"
        symbol2 = "✂."

    elif robot == your_turn:
        print("\n\nIt's a tie! Try again.")
        t += 1

    print(f'You chose {your_turn} {symbol1}')
    print(f'Computer chose {robot} {symbol2}')
    i += 1
    counter = i
    Wins = w
    Losses = a
    Ties = t

print('\n\nGame exit.')
