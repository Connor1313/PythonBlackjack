import random
import sys

# CONNOR AOUN
# FINAL PROJECT 2022 IT 4401
# BLACKJACK GAME


# class for a player which has an attribute hand
class Player:
    def __init__(self, hand):
        self.hand = hand


# this function creates a deck of cards by iterating 4 times through a list that has A-K
def create_deck(cards):
    deck = []
    count = 0
    while count < 4:
        for card in cards:
            deck.append(card)
        count += 1
    # this sorts the deck
    random.shuffle(deck)
    return deck


# this function picks a random card from the deck and returns that card. Also removes the card from the deck
def random_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card


# this function picks two random cards from the deck and adds them to a hand that it returns
def deal(deck):
    hand = []
    card1 = random_card(deck)
    card2 = random_card(deck)
    hand.append(card1)
    hand.append(card2)
    return hand


# this function gets the value of a card and returns that value
def get_value(card, key_list, value_list):
    for i in range(len(key_list)):
        if card == key_list[i]:
            card_value = value_list[i]
            return card_value


# this function prints the hand of a player or dealer
def print_list(hand):
    for element in hand:
        sys.stdout.write(str(element) + ' ')


# this function gets the total of the cards values in a hand. Then it returns the total.
def get_total(hand, key_list, value_list):
    count = 0
    total = 0
    while count < len(hand):  # iterates through the hand and adds each cards value to the total.
        total += int(get_value(hand[count], key_list, value_list))
        count += 1
    return total


def main():
    # loops until the player types N
    while True:
        print("WELCOME TO CONNOR'S BLACKJACK GAME")
        play = input("WOULD YOU LIKE TO PLAY Y/N?")
        # checks if the user input is yes or no.
        if play.upper() == 'Y':
            print("------------------")

            # lists of all cards in the deck
            cards = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q",
                     "K"}

            # dictionary for all the card values
            cards_value = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
                           "Q": 10, "K": 10}

            # puts the cards_values keys and values into each their own lists
            key_list = list(cards_value.keys())
            value_list = list(cards_value.values())

            # creates the deck
            deck = create_deck(cards)

            # creates an instance of a Player object for a player and a dealer
            player = Player(deal(deck))
            dealer = Player(deal(deck))

            # gets the card value for each of the players cards
            player_card1_value = get_value(player.hand[0], key_list, value_list)
            player_card2_value = get_value(player.hand[1], key_list, value_list)

            # prints both hands
            print("Dealer Hand: ", dealer.hand[0] + " (hidden card)\n")
            print("Player Hand: ", player.hand[0] + " " + player.hand[1] + "\n")

            # prints the total of the players cards value
            print("Your total: " + str(player_card1_value
                                       + player_card2_value))

            # gets the total of the players cards
            total = get_total(player.hand, key_list, value_list)
            dealer_total = get_total(dealer.hand, key_list, value_list)

            if dealer_total == 22:  # this checks if dealer has two aces and sets the first ace to 1 if they do
                if get_value(dealer.hand[0], key_list, value_list) == 11:
                    dealer.hand[0] = 1
                    total -= 10

            if total == 21 and dealer_total != 21:  # this checks if player has blackjack
                print("You got blackjack you win! (dealer doesn't have blackjack)")
                continue

            if total == 22:  # this checks if user has two aces and sets the first ace to 1 if they do
                if get_value(player.hand[0], key_list, value_list) == 11:
                    print("Your ace changed to a 1 since your total would be over 21")
                    player.hand[0] = 1
                    total -= 10

            while total < 21:  # loops until the players cards total is 21 or greater
                player_choice = input("\nWould you like to hit or stand? type H or S")  # asks the user if they want
                # to hit or stand
                if len(player_choice) != 1 or (player_choice.upper() != 'H' and player_choice.upper() != 'S'):
                    # user input error check
                    print("Not an accepted answer try again")

                # allows the player to hit when they type H
                if player_choice.upper() == 'H':
                    new_card = random_card(deck)  # gets a new card and adds it to the players hand
                    player.hand.append(new_card)

                    total += get_value(new_card, key_list, value_list)  # gets the total for the players cards values
                    count = 0
                    while total > 21 and count < len(player.hand):  # checks if the player has an ace or not if it does,
                        # if the total is over 21 it changes value to a 1 since ace can be 1 or 11
                        if get_value(player.hand[count], key_list, value_list) == 11:
                            player.hand[count] = 1
                            print("Your ace changed to a 1 since your total would be over 21")
                            total -= 10
                            count += 1
                        else:
                            count += 1

                    print("Your hand is now: ", end='')  # prints players hand
                    print_list(player.hand)
                    print("\nYour Total: ", total)
                elif player_choice.upper() == 'S':  # user stands
                    break

            while dealer_total < 17 and total < 21:  # checks if the dealers total is less than 17 which means it
                # should hit
                dealer_new_card = random_card(deck)  # picks a card and appends it to dealers hand
                dealer.hand.append(dealer_new_card)

                dealer_total += get_value(dealer_new_card, key_list, value_list)  # gets the total for the
                # dealers cards values

                count = 0
                while dealer_total > 21 and count < len(
                        dealer.hand):  # checks if the dealer has an ace or not if it
                    # does if the total is over 21 it changes value to a 1 since ace can be 1 or 11
                    if get_value(dealer.hand[count], key_list, value_list) == 11:
                        dealer.hand[count] = 1
                        print("Dealer ace changed to a 1 since your total would be over 21")
                        dealer_total -= 10
                        count += 1
                    else:
                        count += 1
            print("-------------------")  # prints dealer and player's hands
            print("\nDealer hand: ", end='')
            print_list(dealer.hand)
            print("\n")
            print("Player Hand: ", end='')
            print_list(player.hand)
            print("\n-------------------")
            if total == dealer_total:  # each of these are a check for blackjack so that the game follows the rules
                # of official blackjack https://bicyclecards.com/how-to-play/blackjack/
                print("Both dealer and player have the same score so it pushes.")
            if total > 21:
                print("\nYou busted your total:", total, ", is over 21! Dealer wins.")
            if dealer_total > 21 and total <= 21:
                print("Dealer busted and you didn't so you win!")
            if total > dealer_total and total <= 21 and dealer_total <= 21:
                print("You win your total:", total, ",is greater than the dealers total:", dealer_total)
            if total < dealer_total and dealer_total <= 21 and total <= 21:
                print("You lost your total:", total, ",is less than the dealers total:", dealer_total)
            print("-------------------\n")
        else:
            print("Thanks for playing!!") # end of program
            quit()


main()
