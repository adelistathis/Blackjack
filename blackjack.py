import random

# dictionary mapping each card to its game value
cards = {"Ace": 1,
         "2": 2,
         "3": 3,
         "4": 4,
         "5": 5,
         "6": 6,
         "7": 7,
         "8": 8,
         "9": 9,
         "10": 10,
         "Jack": 10,
         "Queen": 10,
         "King": 10}

# tuple containing the 4 different suits of the cards
suits = ("Spades", "Diamonds", "Hearts", "Clubs")

# tuple containing the keys in the "cards" dictionary
card_keys = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")

# keep track of statistics
user_wins = 0
dealer_wins = 0
ties = 0

count = 1

user_choice = "2"

print("Welcome to Blackjack!")
print("In this version, the Ace is only worth 1 (instead of being worth 1 and 11).")

print("-" * 80)

user_list = []
# add a random card (with a random suit) to the user's hand
# NOTE: duplicate cards are allowed since the game is usually played with multiple decks
user_hand = (random.choice(card_keys), random.choice(suits))
user_list.append(user_hand)
value_of_user_hand = cards[user_hand[0]]

dealer_list = []
# add a random card (with a random suit) to the dealer's hand
dealer_hand = (random.choice(card_keys), random.choice(suits))
dealer_list.append(dealer_hand)
value_of_dealer_hand = cards[dealer_hand[0]]
print("Here is your first card for the round: {} ".format(user_hand))
print("And here is the dealer's first card for the round: {}".format(dealer_hand))

while user_choice != "-1":
    if count == 0:
        print("-" * 80)
        user_list = []
        user_hand = (random.choice(card_keys), random.choice(suits))
        user_list.append(user_hand)
        value_of_user_hand = cards[user_hand[0]]

        dealer_list = []
        dealer_hand = (random.choice(card_keys), random.choice(suits))
        dealer_list.append(dealer_hand)
        value_of_dealer_hand = cards[dealer_hand[0]]

        print("Here is your first card for the round: {} ".format(user_hand))
        print("And here is the dealer's first card for the round: {}".format(dealer_hand))

    if user_choice != "0":
        user_choice = input("What would you like to do? Enter 0 to stick, 1 to hit, or -1 to quit the game: ")

    if user_choice == "0": # deals with the possibility that the user decides to "stick"
        print("-" * 80)
        print("Value of Dealer's hand is now being calculated...")
        # rules state that the dealer must keep hitting while their hand is less than 17
        while value_of_dealer_hand < 17:
            print("-" * 80)
            dealer_hand = (random.choice(card_keys), random.choice(suits))
            dealer_list.append(dealer_hand)
            value_of_dealer_hand += cards[dealer_hand[0]]
            print("Card for dealer: {} ".format(dealer_hand))

        print("-" * 80)
        print("Final Value of Your Hand: ", value_of_user_hand)
        print("Final Value of Dealer's Hand: ", value_of_dealer_hand)
        print("-" * 80)

        # determines whether the user won, the dealer won, or the user and dealer tied
        if value_of_dealer_hand > value_of_user_hand and value_of_dealer_hand <= 21:
            dealer_wins += 1
            user_choice = input("The dealer wins this round! Would you like to start a new round? "
                                "Enter -1 for 'no' and 1 for 'yes': ")
            count = 0
        elif value_of_dealer_hand == value_of_user_hand:
            ties += 1
            user_choice = input("You tied with the dealer. Would you like to start a new round?"
                                "Enter -1 for 'no' and 1 for 'yes': ")
            count = 0
        elif  21 < value_of_dealer_hand < value_of_user_hand:
            dealer_wins += 1
            user_choice = input("The dealer wins this round! Would you like to start a new round? "
                                "Enter -1 for 'no' and 1 for 'yes': ")
            count = 0
        elif value_of_dealer_hand <= 21 and value_of_user_hand > 21:
            dealer_wins += 1
            user_choice = input("The dealer wins this round! Would you like to start a new round? "
                                "Enter -1 for 'no' and 1 for 'yes': ")
            count = 0
        # handles all possibilities where the user wins
        else:
            user_wins += 1
            user_choice = input("You win this round! Would you like to start a new round? "
                                "Enter -1 for 'no' and 1 for 'yes': ")
            count = 0

    else: # deals with the possibility that the user decides to "hit"
        print("-" * 80)
        user_hand = (random.choice(card_keys), random.choice(suits))
        user_list.append(user_hand)
        value_of_user_hand += cards[user_hand[0]]
        print("Your next card: {}".format(user_hand))
        print("Your current hand: {}".format(user_list))
        print("-" * 80)

        # determines if the user can still hit, got blackjack, or busted
        if value_of_user_hand < 21:
            count = 1
        elif value_of_user_hand == 21:
            print("You got blackjack! But the dealer could get it too...")
            count = 1
            user_choice = "0" # the user got blackjack, so they automatically stick
        elif value_of_user_hand > 21:
            print("You busted! But there is still a chance that you can win...")
            user_choice = "0" # the user cannot hit anymore, so we tell the computer that they choose to stick
            count = 1

print("-" * 80)

# prints the final statistics
print("Number of Times You Won: {}".format(user_wins))
print("Number of Times The Dealer Won: {}".format(dealer_wins))
print("Number of Ties: {}".format(ties))
print("Number of Rounds Played: {}".format(user_wins+dealer_wins))

print("-" * 80)

print("Bye! Hope you had fun playing!")