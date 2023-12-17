from abc import ABC, abstractmethod

# Абстрактні класи для продуктів
class Game(ABC):
    @abstractmethod
    def play(self) -> str:
        pass

class SlotMachine(Game):
    def play(self) -> str:
        return "Playing Slot Machine"

class Poker(Game):
    def play(self) -> str:
        return "Playing Poker"

# Абстрактна фабрика
class CasinoFactory(ABC):
    @abstractmethod
    def create_game(self) -> Game:
        pass

# Конкретні фабрики
class SlotMachineFactory(CasinoFactory):
    def create_game(self) -> SlotMachine:
        return SlotMachine()

class PokerFactory(CasinoFactory):
    def create_game(self) -> Poker:
        return Poker()

# Клас, який використовує абстрактну фабрику
class Casino:
    def init(self, game_factory: CasinoFactory):
        self.game_factory = game_factory

    def play_game(self):
        game = self.game_factory.create_game()
        print(f"Let's play: {game.play()}")

# Приклад використання
slot_machine_factory = SlotMachineFactory()
poker_factory = PokerFactory()

casino1 = Casino(slot_machine_factory)
casino1.play_game()

casino2 = Casino(poker_factory)
casino2.play_game()
