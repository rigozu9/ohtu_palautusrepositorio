from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.prompt import Prompt


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("[italic]Nhl statistics by nationality[italic]")

    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

    selected_season = Prompt.ask("Select season", choices=seasons)

    for player in players:
        print(f"[bold magenta]{player}[bold magenta]", ":vampire:")

if __name__ == "__main__":
    main()
