from player import Player

class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = []
    
    def top_scorers_by_nationality(self, nationality):
        for player_dict in self._reader.read():
            player = Player(player_dict)
            if player.nationality == nationality:
                self._players .append(player)

        sorted_players = sorted(self._players, key=lambda x: x.goals + x.assists, reverse=True)

        return sorted_players