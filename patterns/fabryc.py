from abc import ABC, abstractmethod

class CasinoGame(ABC):
    @abstractmethod
    def play(self):
        pass

class Roulette(CasinoGame):
    def play(self):
        return "Це гра в рулетку"

class Blackjack(CasinoGame):
    def play(self):
        return "Це гра в блекджек"

class CasinoGameFactory(ABC):
    @abstractmethod
    def create_game(self):
        pass

class RouletteFactory(CasinoGameFactory):
    def create_game(self):
        return Roulette()

class BlackjackFactory(CasinoGameFactory):
    def create_game(self):
        return Blackjack()

class Casino:
    def init(self, game_factory):
        self.game_factory = game_factory

    def start_game(self):
        game = self.game_factory.create_game()
        return game.play()

if name == "main":
    # Використовуємо фабрику для створення гри в рулетку
    roulette_factory = RouletteFactory()
    casino_roulette = Casino(roulette_factory)
    roulette_game = casino_roulette.start_game()
    print(roulette_game)  # Виведе "Це гра в рулетку"

    # Використовуємо фабрику для створення гри в блекджек
    blackjack_factory = BlackjackFactory()
    casino_blackjack = Casino(blackjack_factory)
    blackjack_game = casino_blackjack.start_game()
    print(blackjack_game)  # Виведе "Це гра в блекджек"
