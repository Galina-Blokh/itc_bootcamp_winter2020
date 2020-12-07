import random

# Complete all

modes = ["rock", "paper", "scissors"]


def comp_turn(modes):
    """The choice made by the computer"""
    comp = random.choice(modes)  # Comp should get a random choice from the list modes. use the "random" package
    return comp


def calc_win(comp, move):
    """Determining the win"""
    print("The computer chose {0}.".format(comp))
    win = None  # refactor the name of the "win" variable, to "win" shft+F6+Rename all
    tie = False

    if move == comp:
        print("No winner.... Restarting....\n")
        main()
        tie = True
    elif ((comp == "rock") and (move == "paper")) or \
            ((comp == "paper") and (move == "scissors")) or \
            ((comp == "scissors") and (move == "rock")):
        win = True
    else:
        win = False

    return win, tie


def player_turn():  # using only the keyboard, lower this function to under "calc_win" ctrl+shft+down
    """The choice made by the user"""
    move = ""
    while move not in modes:
        move = input("Choose your move (rock, paper, or scissors: ").lower()
    return move


def print_winner(win, tie):
    """Display the winner of the game."""
    if tie == True:
        print("")
    elif win == True:
        print("You beat the computer!")
    elif win == False:
        print("The computer beat you!")


def main():
    """This is the main function"""
    comp = comp_turn(modes)
    move = player_turn()  # jump to the function "calc_win" using Ctrl + press on function name and change the
    # print statement to: "No winner.... Restarting...."
    win, tie = calc_win(comp, move)
    print_winner(win, tie)


main()
#  prettify your code using reformatting (Ctrl + A, and then Ctrl + Alt + L)
#  delete all statements
