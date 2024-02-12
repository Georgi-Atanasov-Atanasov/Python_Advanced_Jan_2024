def team_lineup(*args):
    player_country_info = {}
    for data in args:
        name = data[0]
        country = data[1]
        if country not in player_country_info:
            player_country_info[country] = []
        player_country_info[country].append(name)
    player_country_info = sorted(player_country_info.items(), key=lambda team: (-len(team[1]), team[0]))
    result = ""
    for country, players in player_country_info:
        result += f'{country}:\n'
        for player in players:
            result += f'  -{player}\n'
    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

