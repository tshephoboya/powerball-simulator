from draw import Draw
from players import Player

draw = Draw()
draw.get_numbers()
players = Player.generate_players()

def run_app():
    for player in players:
        matched_numbers = list(filter(lambda number: number in draw.numbers, player.numbers))
        player.matched['Numbers'] = len(matched_numbers)
        if player.powerball == draw.powerball:
            player.matched['Powerball'] = True

        player.calc_winning()
        print(player.name, 'Won', '${}'.format(player.winnings))

    command = input('Do you want to run again? y/n ')
    if command.lower() == 'y':
        run_app()

run_app()
