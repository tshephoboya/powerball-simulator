import random
import constants

class Player:
    def __init__(self, name):
        self.name = name
        self.numbers = list()
        self.powerball = None
        self.matched = {'Numbers': None, 'Powerball': False}
        self.winnings = None

    def player_numbers(self):
        self.numbers = random.sample(range(1, constants.CONSTANTS_NUMBERS_MAX), 5)

    def player_powerball(self):
        self.powerball = random.choice(range(1, constants.CONSTANTS_POWERBALL_MAX))

    def calc_winning(self):
        self.winnings = self.matched['Numbers'] ** 10
        if self.matched['Powerball']:
            self.winnings += 10000000


    @classmethod
    def generate_players(cls):
        try:
            num_players = int(input('How many players do you want to simulate?  Max 100 '))
        except ValueError:
            cls.generate_players()

        if num_players > 100:
            cls.generate_players()

        players = [Player('player {}'.format(i)) for i in range(num_players)]

        for player in players:
            player.player_numbers()
            player.player_powerball()

        return players

    def __repr__(self):
        return '<Player name is {} >'.format(self.name)


