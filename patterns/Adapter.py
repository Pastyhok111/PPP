from flask import Flask, render_template
import copy

app = Flask(name)

class Casino:
    def init(self, name, theme, table_count, entry_fee):
        self.name = name
        self.theme = theme
        self.table_count = table_count
        self.entry_fee = entry_fee

class CasinoService:
    def get_casino_list(self):
        pass

    def get_casino_details(self, casino_name):
        pass

class CasinoUI:
    def show_casino_list(self):
        pass

    def show_casino_details(self, casino_name):
        pass

class CasinoAdapter(CasinoUI):
    def init(self, casino_service):
        self.casino_service = casino_service

    def show_casino_list(self):
        return self.casino_service.get_casino_list()

    def show_casino_details(self, casino_name):
        return self.casino_service.get_casino_details(casino_name)

class CasinoServiceImpl(CasinoService):
    def init(self):
        self.catalog = []

    def add_casino(self, casino):
        self.catalog.append(casino)

    def get_casino_list(self):
        return copy.deepcopy(self.catalog)

    def get_casino_details(self, casino_name):
        for casino in self.catalog:
            if casino.name == casino_name:
                return casino

casino_service_impl = CasinoServiceImpl()
casino_adapter = CasinoAdapter(casino_service_impl)

# Початковий список казино
original_casinos = [
    Casino("Luxury Casino", "Elegant", 20, 50.0),
    Casino("Classic Casino", "Classic", 15, 30.0),
    Casino("Vegas Casino", "Modern", 30, 75.0)
]

# Додаємо казино до каталогу
for casino in original_casinos:
    casino_service_impl.add_casino(casino)

@app.route('/')
def index():
    casinos = casino_adapter.show_casino_list()
    return render_template('index_adapter.html', casinos=casinos)

@app.route('/casinos/<casino_name>')
def casino_details(casino_name):
    casino_details = casino_adapter.show_casino_details(casino_name)
    return render_template('casino_details_adapter.html', casino=casino_details)

if name == 'main':
    app.run(debug=True)
