from Form_Deck import Deck








deck = Deck()
deck.build()
deck.shuffle()


#this will be the initial deal to start each game
def initial_deal():
    global card1
    # the first entry in these lists is a boolian for whether the hand is a bust
    global player_cards
    global computer_cards
    player_cards = [False]
    computer_cards = [False]
    card1 = deck.draw()
    computer_cards.append(card1.value)
    card = deck.draw()
    print(f'player is delt {card}')
    player_cards.append(card.value)
    card = deck.draw()
    print(f'Dealer is showing a {card}')
    computer_cards.append(card.value)
    card = deck.draw()
    print(f'player is delt {card}')
    player_cards.append(card.value)
    print('players count is ' + str(sum(player_cards[1:])))
    check_bust(player_cards)

#This is for the player to draw a card
def player_draw():
    card = deck.draw()
    print(f'player is delt {card}\n')
    player_cards.append(card.value)
    print('players count is ' + str(sum(player_cards[1:])))
    check_bust(player_cards)

#this is for the computer draw the first time
def computer_draw_1st():
    print(f'Dealer flips {card1}\n')
    print('The dealers count is ' + str(sum(computer_cards[1:])))
    check_bust(computer_cards)
    if sum(computer_cards) < 16 and sum(player_cards[1:]) <= 22:
        card = deck.draw()
        print(f'\nDealer deals self a {card}\n')
        computer_cards.append(card.value)
        print('The dealers count is ' + str(sum(computer_cards[1:])))
        check_bust(computer_cards)

#this is for the rest of the computer draws
def computer_draw_else():
    if sum(computer_cards[1:]) < 16:
        card = deck.draw()
        print(f'\nDealer deals self a {card}\n')
        computer_cards.append(card.value)
        print('The dealers count is ' + str(sum(computer_cards[1:])))
        check_bust(computer_cards)

def check_bust(hand):
    if sum(hand[1:]) < 21:
        pass
    elif sum(hand[1:]) == 21:
        print('BlackJack!')
    elif sum(hand[1:]) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        print('Your Ace is now a 1.\n\n')
        print('The count is ' + str(sum(hand[1:])))
    else:
        print('Bust!')
        hand[0] = True




if __name__ == '__main__':
    initial_deal()
    input()
    player_draw()
    input()
    check_bust(player_cards)
    input()
    computer_draw_1st()
    input()
    check_bust(computer_cards)