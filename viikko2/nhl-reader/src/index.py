from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.table import Table

def main():
    print("[italic]Nhl statistics by nationality[italic]\n")

    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

    nationalities = [
        "AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", 
        "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"
    ]

    selected_season = Prompt.ask("Select season", choices=seasons)

    url = f"https://studies.cs.helsinki.fi/nhlstats/{selected_season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        selected_nationality = Prompt.ask("Select nationality (type 'exit' to close)", choices=nationalities + ["exit"])
        
        if selected_nationality == "exit":
            print("[bold red]Exiting... Goodbye!")
            break

        print(f"[italic]Top scorers of {selected_nationality} season {selected_season}[italic]\n")

        players = stats.top_scorers_by_nationality(selected_nationality)

        table = Table(title=f"Top scorers of {selected_nationality} season {selected_season}")

        table.add_column("Name", style="cyan", justify="left")
        table.add_column("Team", style="magenta", justify="center")
        table.add_column("Goals", style="green", justify="right")
        table.add_column("Assists", style="blue", justify="right")
        table.add_column("Points", style="yellow", justify="right")

        for player in players:
            table.add_row(
                player.name, player.team, 
                str(player.goals), str(player.assists), str(player.goals + player.assists)
            )

        print(table)
        print("\n")

if __name__ == "__main__":
    main()
