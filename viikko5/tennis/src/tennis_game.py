class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        self.player1_score += 1 if player_name == self.player1_name else 0
        self.player2_score += 1 if player_name == self.player2_name else 0

    def get_point_name(self, score):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names.get(score)

    def get_drawing_score(self):
        drawing_scores = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return drawing_scores.get(self.player1_score, "Deuce")

    def get_advantage_score(self):
        score_difference = self.player1_score - self.player2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_regular_score(self):
        player1_point = self.get_point_name(self.player1_score)
        player2_point = self.get_point_name(self.player2_score)
        return f"{player1_point}-{player2_point}"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_drawing_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_advantage_score()
        else:
            return self.get_regular_score()
