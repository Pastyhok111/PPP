# Пример реализации шаблона Builder для построения объекта "Казино"

class CasinoBuilder:
    def init(self):
        self.casino = Casino()

    def set_size(self, size):
        pass

    def set_table_count(self, table_count):
        pass

    def set_theme(self, theme):
        pass

    def get_casino(self):
        return self.casino


class Casino:
    def init(self):
        self.size = None
        self.table_count = None
        self.theme = None

    def str(self):
        return f"Казино: размер - {self.size}, количество игровых столов - {self.table_count}, тема - {self.theme}"


class FancyCasinoBuilder(CasinoBuilder):
    def set_size(self, size):
        self.casino.size = f"Роскошное {size}"
        return self

    def set_table_count(self, table_count):
        self.casino.table_count = table_count + 10
        return self

    def set_theme(self, theme):
        self.casino.theme = f"Элегантное казино в стиле {theme}"
        return self


class SimpleCasinoBuilder(CasinoBuilder):
    def set_size(self, size):
        self.casino.size = f"Обычное {size}"
        return self

    def set_table_count(self, table_count):
        self.casino.table_count = table_count
        return self

    def set_theme(self, theme):
        self.casino.theme = f"Простое казино в стиле {theme}"
        return self


# Пример использования

fancy_casino_builder = FancyCasinoBuilder()
fancy_casino = fancy_casino_builder.set_size("большое").set_table_count(20).set_theme("ретро").get_casino()
print(fancy_casino)

simple_casino_builder = SimpleCasinoBuilder()
simple_casino = simple_casino_builder.set_size("среднее").set_table_count(10).set_theme("модерн").get_casino()
print(simple_casino)
