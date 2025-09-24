def calculate_football_ranking(teams_list):
    processed_teams = []
    for team in teams_list:
        points = (team["wins"] * 3) + (team["draws"] * 1)
        goal_difference = team["scored"] - team["conceded"]
        processed_teams.append({
            "name": team["name"],
            "points": points,
            "gd": goal_difference
        })

    n = len(processed_teams)
    for i in range(n):
        for j in range(0, n - i - 1):
            current_team = processed_teams[j]
            next_team = processed_teams[j+1]
            if current_team["points"] < next_team["points"]:
                processed_teams[j], processed_teams[j+1] = processed_teams[j+1], processed_teams[j]

            elif current_team["points"] == next_team["points"]:
                if current_team["gd"] < next_team["gd"]:
                    processed_teams[j], processed_teams[j+1] = processed_teams[j+1], processed_teams[j]
    return processed_teams



input_str = input("Enter Input : ")
teams_str_list = input_str.split('/')
football_data = []
for team_data in teams_str_list:
    parts = team_data.split(',')
    team = {
        "name": parts[0],
        "wins": int(parts[1]),
        "loss": int(parts[2]),
        "draws": int(parts[3]),
        "scored": int(parts[4]),
        "conceded": int(parts[5])
    }
    football_data.append(team)

print("== results ==")
for team in calculate_football_ranking(football_data):
    print(f"['{team['name']}', {{'points': {team['points']}}}, {{'gd': {team['gd']}}}]")