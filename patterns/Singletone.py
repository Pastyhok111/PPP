# app.py
from flask import Flask, render_template
import copy

app = Flask(name)

class Casino:
    def init(self, name, theme, table_count, entry_fee):
        self.name = name
        self.theme = theme
        self.table_count = table_count
        self.entry_fee = entry_fee

class CasinoCatalogSingleton:
    _instance = None

    def new(cls):
        if not cls._instance:
            cls._instance = super(CasinoCatalogSingleton, cls).new(cls)
            cls._instance.catalog = []
        return cls._instance

    def add_casino(self, casino):
        self.catalog.append(casino)

    def get_catalog(self):
        return copy.deepcopy(self.catalog)

casino_catalog = CasinoCatalogSingleton()

# Початковий список казино
original_casinos = [
    Casino("Luxury Casino", "Elegant", 20, 50.0),
    Casino("Classic Casino", "Classic", 15, 30.0),
    Casino("Vegas Casino", "Modern", 30, 75.0)
]

# Додаємо казино до каталогу
for casino in original_casinos:
    casino_catalog.add_casino(casino)

@app.route('/')
def index():
    return render_template('index_singleton.html', casinos=casino_catalog.get_catalog())

@app.route('/casinos')
def casinos():
    cloned_casinos = [casino.clone() for casino in original_casinos]
    return render_template('casinos.html', casinos=cloned_casinos)

if name == 'main':
    app.run(debug=True)
