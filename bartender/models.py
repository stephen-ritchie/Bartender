from . import db


class Pump(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    pin = db.Column(db.String(1000))
    value = db.Column(db.String(1000))

    def __init__(self, name, pin, value):
        self.name = name
        self.pin = pin
        self.value = value
