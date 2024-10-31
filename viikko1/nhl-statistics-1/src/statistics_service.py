from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class StatisticsService:
    def __init__(self, reader):
        reader = reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # onko = False
        # if sort_by == SortBy.POINTS:
        #     onko = True
        
        # # print("oikein vai v äärin sort_by=SortBy.POINTS", onko)
        # metodin käyttämä apufufunktio voidaan määritellä näin
        # def sort_by_filter(player):
        #     if sort_by == SortBy.POINTS:
        #         return player.points
        #     if sort_by == SortBy.GOALS:
        #         return player.goals
        #     if sort_by == SortBy.ASSISTS:
        #         return player.assists

        #helpompi versio sanakirjaa käyttäen
        sort_key_map = {
            SortBy.POINTS: lambda player: player.points,
            SortBy.GOALS: lambda player: player.goals,
            SortBy.ASSISTS: lambda player: player.assists
        }

        sort_key_function = sort_key_map[sort_by]

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_key_function
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        # print("first on the list", result[0].name)
        return result
