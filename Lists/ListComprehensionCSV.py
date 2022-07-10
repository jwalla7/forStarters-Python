import csv

header = ["player", "team", "age", "ppg", "pts"]
data = (
    ("Joel Embiid", "PHI", int(28), float(30.6), int(2079)),
    ("LeBron James", "LAL", int(37), float(30.3), int(1695)),
    ("Giannis Antetokounmpo", "MIL", int(27), float(29.9), int(2002)),
    ("Kevin Durant", "BKN", int(33), float(29.9), int(1643)),
    ("Luka Doncic", "DAL", int(23), float(28.4), int(1847)),
    ("Trae Young", "ATL", int(23), float(28.4), int(2155)),
    ("DeMar DeRozan", "CHI", int(32), float(27.9), int(2118)),
    ("Kyrie Irving", "BKN", int(30), float(27.4), int(796)),
    ("Ja Morant", "MEM", int(22), float(27.4), int(1564)),
    ("Nikola Jokic", "DEN", int(27), float(27.1), int(2004))
)

# open file in write mode
with open('/Users/jwalla7/PycharmProjects/forStarters-Python/Lists/csv_players.csv', 'w', encoding='UTF-8') as filename:
    # create csv writer
    writer = csv.writer(filename)
    # write the Header row
    writer.writerow(header)
    # write the Data rows
    writer.writerows(data)
    # close file
    filename.close()


# player_info =

def read_player_report(filename, *, errors='warn'):
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn','silent','raise'")

    players = []
    with open(filename, 'r') as r_player_report:
        rows = csv.reader(r_player_report)
        headers = next(rows)  # Skip the header row
        for row_no, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
                row[4] = int(row[4])
            except ValueError as v_err:
                if errors == 'warn':
                    print('Row:', row_no, 'Bad row:', row)
                    print('Row:', row_no, 'Reason', v_err)
                elif errors == 'raise':
                    raise  # Reraises last exception
                else:
                    pass  # Ignore
                continue  # Skips to the next row

            report = {
                "player": row[0],
                "team": row[1],
                "age": row[2],
                "ppg": row[3],
                "pts": row[4]
            }
            players.append(report)
    return players


players = read_player_report('/Users/jwalla7/PycharmProjects/forStarters-Python/Lists/csv_players.csv')
print(type(players))

print("------ [List] Players Reported ------")
players_names = [player_name['player'] for player_name in players]
print(players_names)


print("------ [List] Players Reported Over Age of 30 ------")
players_over_30 = [player['player'] for player in players if player['age'] > 30]
print(players_over_30)


print("------ {Dict} Player/Stats Reported ------")
for player_stats in players:
    print(player_stats)

print("------ [List] Teams Reported (Unordered) ------")
# For-in
reported_teams = []
for player_stats in players:
    if 'team' in player_stats and player_stats['team'] not in reported_teams:
        reported_teams.append(player_stats['team'])
print("for-in:", reported_teams)
# Set
player_teams = [player['team'] for player in players]
reported_teams_set = set(player_teams)
print("set:", reported_teams_set)
# Set Comprehension
reported_teams_set_comp = {player['team'] for player in players}
print("set comp:", reported_teams_set_comp)


print("------ Total Pts of Players Reported ------")
players_total_pts = sum([player_stats['pts'] for player_stats in players])
print(players_total_pts)
