import sys
import random


def if_bet_correct(b, am):
    if not b.isdigit():
        print("it is not a digit i expected >:( i don't play with cheater. buy!")
        sys.exit()
    elif int(b) <= 0 or int(b) > am:
        print("it is not in allowed range, i don't play with cheater. buy!")
        sys.exit()
    else:
        return True


def game(d1, d2, b, am):
    count_amount = am
    random.shuffle(d1)
    random.shuffle(d2)
    while d1 and d2 and if_bet_correct(b, count_amount):
        player, comp = d1.pop(), d2.pop()
        print(player, comp)
        if player > comp:
            count_amount += int(b)
            print('Your card is', player, 'My card is', comp)
            print('You won', b, 'NIS', 'now you have', count_amount, 'NIS')
        else:
            count_amount -= int(b)
            print('Your card is', player, 'My card is', comp)
            print('You lost', b, 'NIS', 'now you have', count_amount)
        if count_amount <= 0:
            return count_amount
        elif offer():
            b = input('Place your bet for the next round: 1 to ' + str(count_amount) + '\n ')
        else:
            print('Ok, you can go with your', count_amount, 'NIS')
            sys.exit()
    return count_amount


def offer():
    print('What would you like to do?\n 1.Play another round\n 2.Go with my money ;-p ')
    a = 0
    while a != "1" or a != "2":
        a = input('enter "1" or "2"\n')
        if a == "1":
            return True
        elif a == "2":
            return False


def decision(amount, bet):
    if amount <= 0:
        print('you are broke ..... buy-buy!!!...')
        sys.exit()
    elif amount > 0:
        amount -= int(bet)
        print('You are not win . But Your amount is', amount, 'NIS')
        if not offer():
            print('Ok, you can go with your', amount, 'NIS')
            sys.exit()
    else:
        amount += int(bet)
        print('You are win', bet, 'NIS, and now you have', amount, 'NIS')


print()
print()
print('////////------------Welcome To WAR------------\\\\\\\\\\\\\\\\')
print()
name = input('please enter your name ' + '\n')
amount = 50
print('Hello', name, 'You currently have', amount, 'ILS')
bet = input('Place your bet for the next round: 1 to ' + str(amount) + '\n ')
dk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
while amount > 0:
    points = 0
    while if_bet_correct(bet, amount):
        deck1 = dk1.copy()
        deck2 = dk1.copy()
        amount = game(deck1, deck2, bet, amount)
        decision(amount, bet)
