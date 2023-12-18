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

    def clone(self):
        return copy.deepcopy(self)

class PrototypeManager:
    def init(self):
        self.prototypes = {}

    def add_prototype(self, name, prototype):
        self.prototypes[name] = prototype

    def get_prototype(self, name):
        return self.prototypes.get(name)

prototype_manager = PrototypeManager()

# Початковий список казино
original_casinos = [
    Casino("Luxury Casino", "Elegant", 20, 50.0),
    Casino("Classic Casino", "Classic", 15, 30.0),
    Casino("Vegas Casino", "Modern", 30, 75.0)
]

# Додайте казино до менеджера прототипів
for casino in original_casinos:
    prototype_manager.add_prototype(casino.name, casino)

@app.route('/')
def index():
    return render_template('index.html', casinos=original_casinos)

@app.route('/casinos')
def casinos():
    cloned_casinos = [casino.clone() for casino in original_casinos]
    return render_template('casinos.html', casinos=cloned_casinos)

if name == 'main':
    app.run(debug=True)
