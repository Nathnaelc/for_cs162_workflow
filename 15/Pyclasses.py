import random


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [{'Suit': suit, 'Value': value}
                     for suit in suits for value in values]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.hand:
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


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.setup()

    def setup(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def player_action(self):
        action = input(
            "Do you want to Hit or Stand? (Enter 'hit' or 'stand'): ").lower()
        if action == 'hit':
            self.player_hand.add_card(self.deck.deal())

    def dealer_action(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal())

    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if player_value > dealer_value:
            return 'Player wins!'
        elif dealer_value > player_value:
            return 'Dealer wins!'
        else:
            return 'It\'s a tie!'

    def play(self):
        while True:
            print("Player's hand:", [(card['Value'], card['Suit'])
                  for card in self.player_hand.hand])
            print("Dealer's first card:",
                  (self.dealer_hand.hand[0]['Value'], self.dealer_hand.hand[0]['Suit']))

            player_value = self.player_hand.calculate_value()
            if player_value == 21:
                print('Blackjack')
                break
            elif player_value > 21:
                print('Bust')
                break

            self.player_action()

        self.dealer_action()
        print("Dealer's hand:", [(card['Value'], card['Suit'])
              for card in self.dealer_hand.hand])

        winner = self.determine_winner()
        print(winner)


if __name__ == "__main__":
    game = Game()
    game.play()
