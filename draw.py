import datetime
import random
import constants

class Draw:
    def __init__(self):
        self.seed = None
        self.date = datetime.date.today()
        self.numbers = list()
        self.powerball = None

    def __get_seed(self):
        datenow = str(datetime.datetime.now())
        date_list = list(filter(lambda char: char.isdigit(), datenow))
        date_list = list(map(lambda char: int(char), date_list))
        self.seed = sum(date_list)

    def get_numbers(self):
        self.__get_seed()
        random.seed(self.seed)
        self.numbers = random.sample(range(1, constants.CONSTANTS_NUMBERS_MAX), 5)
        self.powerball = random.choice(range(1, constants.CONSTANTS_POWERBALL_MAX))

    def __repr__(self):
        return '<The draw date is : {} >'.format(self.date)
