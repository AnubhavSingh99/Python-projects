import random
class Player:
    def __init__(self, name, is_impostor=False):
        self.name = name
        self.is_impostor = is_impostor

class AmongUsGame:
    def __init__(self, players):
        self.players = players
        self.impostors = [player for player in players if player.is_impostor]
        self.crewmates = [player for player in players if not player.is_impostor]

    def print_players(self):
        print("Players:")
        for player in self.players:
            print(player.name)

    def emergency_meeting(self):
        print("Emergency Meeting!")
        for player in self.players:
            print(f"{player.name} is voting...")
            if player.is_impostor:
                vote = random.choice(self.crewmates)
            else:
                vote = random.choice(self.players)
            print(f"{player.name} votes for {vote.name}")
        print("Voting results:")
        ejected = max(set(self.players), key=self.players.count)
        print(f"{ejected.name} was ejected!")
print("jj")
# Example Usage
player1 = Player("Player 1", is_impostor=True)
player2 = Player("Player 2")
player3 = Player("Player 3")
player4 = Player("Player 4")
player5 = Player("Player 5")

players_list = [player1, player2, player3, player4, player5]

among_us_game = AmongUsGame(players_list)
among_us_game.print_players()
among_us_game.emergency_meeting()
