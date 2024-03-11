# basket_ball.py

def game_dict():
    # Provided function returning the nested dictionary
    return {
        'home': {
            'team_name': 'Cleveland Cavaliers',
            'colors': ['Gold', 'Wine'],
            'players': {
                'Alan Anderson': {
                    'number': 0,
                    'shoe': 16,
                    'points': 22,
                    'rebounds': 12,
                    'assists': 12,
                    'steals': 3,
                    'blocks': 1,
                    'slam_dunks': 1
                },
                # Other players omitted for brevity
            }
        },
        'away': {
            'team_name': 'Charlotte Hornets',
            'colors': ['Turquoise', 'Purple'],
            'players': {
                'Jeff Adrien': {
                    'number': 4,
                    'shoe': 18,
                    'points': 10,
                    'rebounds': 1,
                    'assists': 1,
                    'steals': 2,
                    'blocks': 7,
                    'slam_dunks': 2
                },
                # Other players omitted for brevity
            }
        }
    }

def num_points_per_game(player_name):
    # Function to get the number of points per game for a given player
    players = game_dict()['home']['players']
    players.update(game_dict()['away']['players'])
    if player_name in players:
        return players[player_name]['points']  # Return points if player exists
    else:
        return "Player not found"

def player_age(player_name):
    # Function to get the age of a given player
    players = game_dict()['home']['players']
    players.update(game_dict()['away']['players'])
    if player_name in players:
        if 'age' in players[player_name]:
            return "Age: {}".format(players[player_name]['age'])
        else:
            return "Age information not available for this player"
    else:
        return "Player not found"

def team_colors(team_name):
    # Function to get the colors of a given team
    teams = game_dict()
    for location in teams:
        if teams[location]['team_name'] == team_name:
            return teams[location]['colors']
    return "Team not found"

def team_names():
    # Function to get a list of team names
    return [game_dict()['home']['team_name'], game_dict()['away']['team_name']]

def player_numbers(team_name):
    # Function to get a list of jersey numbers for a given team
    teams = game_dict()
    for location in teams:
        if teams[location]['team_name'] == team_name:
            return [players['number'] for players in teams[location]['players'].values()]
    return "Team not found"

def player_stats(player_name):
    # Function to get the stats of a given player
    players = game_dict()['home']['players']
    players.update(game_dict()['away']['players'])
    if player_name in players:
        return players[player_name]
    else:
        return "Player not found"



# Example usage:
print(num_points_per_game("Jeff Adrien"))
print(player_age("Jeff Adrien"))
print(team_colors("Cleveland Cavaliers"))
print(team_names())
print(player_numbers("Charlotte Hornets"))
print(player_stats("Jeff Adrien"))
average_rebounds_by_shoe_brand()
