#This will be the main program for the Black Jack game
from Player_Bank import Account
import Deal




def Main_menu():
    go = True
    while go:
        try:
            answer = int(input('Welcome to Black Jack by Tyler!\n\nWhat would you like to do?\n\n(1) Start game\n(2)Exit\n\n'))
            if answer == 1:
                go = False
                Bank_amount()
            elif answer == 2:
                print('Goodbye!')
                break
        except ValueError:
            print('\nAn error occurred\n')
            pass



def Bank_amount():
    global balance
    try:
        name = input('Please enter your name?\n\n')
        answer = int(input('Please enter the amount of money you wish to start with.\n\n'))
        balance = Account(name,answer)

    except:
        print('An error occured.')
        Bank_amount()


def Betting():
    global bet
    print(balance)
    try:
        bet = int(input('\n\nHow much would you like to bet?\n'))
        if bet <= balance.balance:
            balance.bet(bet)
        else:
            print('\nYou do not have enough for this bet.\n')
            Betting()
    except ValueError:
        print('\nAn error occurred\n')
        Betting()



def Player_bust():
    if Deal.player_cards[0] is True:
        print('Player has busted!')

def Computer_bust():
    global balance
    if Deal.computer_cards[0] is True:
        print('Dealer has busted!')


def Check_win():
    if sum(Deal.player_cards[1:]) > sum(Deal.computer_cards[1:]) and Deal.player_cards[0] is False or Deal.computer_cards[0] is True:
        balance.win(bet * 2)
    elif sum(Deal.player_cards[1:]) == sum(Deal.computer_cards[1:]):
        balance.win(bet)
    else:
        pass



def Black_Jack_Baby():
    Main_menu()
    game_on = True
    while game_on:
        Betting()
        Deal.initial_deal()
        hitting = True
        while hitting:
            if sum(Deal.player_cards[1:]) >= 21:
                break
            try:
                a = int(input('Would you like to hit or stay?\n(1)Hit\n(2)Stay\n'))
                if a == 1:
                    Deal.player_draw()
                    pass
                elif a == 2:
                    break
                else:
                    pass
            except ValueError:
                print('An error occurred.')
                pass

        Deal.computer_draw_1st()
        Deal.computer_draw_else()
        Check_win()
        if balance.balance == 0:
            print('You Lose')
            Black_Jack_Baby()
        play_again = True
        while play_again:
            try:
                b = int(input('Would you like to play again?\n(1)yes\n(2)no\n'))
                if b == 1:
                    break
                elif b == 2:
                    Black_Jack_Baby()
                else:
                    pass
            except ValueError:
                print('An error occurred.')
                pass

Black_Jack_Baby()