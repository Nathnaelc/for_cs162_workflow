import random

# Initialize a deck of cards


def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'Suit': suit, 'Value': value}
            for suit in suits for value in values]
    return deck

# Shuffle the deck


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal cards to player and dealer


def deal_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

# Calculate the value of a hand


def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card['Value'] in ['J', 'Q', 'K']:
            value += 10
        elif card['Value'] == 'A':
            value += 11
            aces += 1
        else:
            value += int(card['Value'])
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Check for Blackjack or Bust


def check_conditions(hand_value):
    if hand_value == 21:
        return 'Blackjack'
    elif hand_value > 21:
        return 'Bust'
    else:
        return 'Continue'

# Handle player's actions


def player_action(deck, player_hand):
    action = input(
        "Do you want to Hit or Stand? (Enter 'hit' or 'stand'): ").lower()
    if action == 'hit':
        player_hand.append(deck.pop())
    return player_hand

# Handle dealer's actions


def dealer_action(deck, dealer_hand):
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand

# Determine the winner


def determine_winner(player_value, dealer_value):
    if player_value > dealer_value:
        return 'Player wins!'
    elif dealer_value > player_value:
        return 'Dealer wins!'
    else:
        return 'It\'s a tie!'

# Main function to control game flow


def main():
    deck = initialize_deck()
    deck = shuffle_deck(deck)
    player_hand, dealer_hand = deal_cards(deck)

    while True:
        print("Player's hand:", [(card['Value'], card['Suit'])
              for card in player_hand])
        print("Dealer's first card:",
              (dealer_hand[0]['Value'], dealer_hand[0]['Suit']))

        player_value = calculate_hand_value(player_hand)
        condition = check_conditions(player_value)
        if condition != 'Continue':
            print(condition)
            break

        player_hand = player_action(deck, player_hand)

    dealer_hand = dealer_action(deck, dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    print("Dealer's hand:", [(card['Value'], card['Suit'])
          for card in dealer_hand])

    winner = determine_winner(player_value, dealer_value)
    print(winner)


if __name__ == "__main__":
    main()
