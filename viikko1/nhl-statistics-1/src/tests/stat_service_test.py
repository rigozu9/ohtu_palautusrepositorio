import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none(self):
        player = self.stats.search("Riku")
        self.assertEqual(player, None)
    
    def test_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_points(self):
        top = self.stats.top(3)
        self.assertEqual(top[0].name, "Gretzky")

    def test_top_goals(self):
        top = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top[0].name, "Lemieux")

    def test_top_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top[0].name, "Gretzky")
        