import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)

    # print("Oliot:")
    # print(sorted(players, key=lambda x: x.goals + x.assists, reverse=True))
    sorted_players = sorted(players, key=lambda x: x.goals + x.assists, reverse=True)

    for player in sorted_players:
        print(player)

if __name__ == "__main__":
    main()
