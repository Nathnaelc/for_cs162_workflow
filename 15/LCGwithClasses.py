import random
import time


class Blackjack:
    def __init__(self, prng_choice):
        self.deck = self.initialize_deck()
        if prng_choice == 'lcg':
            self.prng = self.lcg(int(time.time()))
        else:
            self.prng = None  # Use Python's built-in Mersenne Twister

    def lcg(self, seed, a=1664525, c=1013904223, m=2**32):
        while True:
            seed = (a * seed + c) % m
            yield seed / m

    def shuffle_deck(self):
        if self.prng:
            for i in reversed(range(1, len(self.deck))):
                j = int(next(self.prng) * (i + 1))
                self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        else:
            random.shuffle(self.deck)

    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [{'Suit': suit, 'Value': value}
                for suit in suits for value in values]
        self.shuffle_deck()
        return deck

    def deal_cards(self):
        return [self.deck.pop(), self.deck.pop()], [self.deck.pop(), self.deck.pop()]

    def calculate_hand_value(self, hand):
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

    def check_conditions(self, hand_value):
        if hand_value == 21:
            return 'Blackjack'
        elif hand_value > 21:
            return 'Bust'
        else:
            return 'Continue'

    def player_action(self, player_hand):
        action = input(
            "Do you want to Hit or Stand? (Enter 'hit' or 'stand'): ").lower()
        if action == 'hit':
            player_hand.append(self.deck.pop())
        return player_hand

    def dealer_action(self, dealer_hand):
        while self.calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(self.deck.pop())
        return dealer_hand

    def determine_winner(self, player_value, dealer_value):
        if player_value > dealer_value:
            return 'Player wins!'
        elif dealer_value > player_value:
            return 'Dealer wins!'
        else:
            return 'It\'s a tie!'

    def play(self):
        player_hand, dealer_hand = self.deal_cards()

        while True:
            print("Player's hand:", [(card['Value'], card['Suit'])
                  for card in player_hand])
            print("Dealer's first card:",
                  (dealer_hand[0]['Value'], dealer_hand[0]['Suit']))

            player_value = self.calculate_hand_value(player_hand)
            condition = self.check_conditions(player_value)
            if condition != 'Continue':
                print(condition)
                break

            player_hand = self.player_action(player_hand)

        dealer_hand = self.dealer_action(dealer_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        print("Dealer's hand:", [(card['Value'], card['Suit'])
              for card in dealer_hand])

        winner = self.determine_winner(player_value, dealer_value)
        print(winner)


if __name__ == "__main__":
    prng_choice = input(
        "Choose PRNG algorithm ('lcg' for Linear Congruential Generator or 'mersenne' for Mersenne Twister): ").strip().lower()
    game = Blackjack(prng_choice)
    game.play()
