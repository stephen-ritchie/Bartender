#!/usr/bin/env python

from bartender import create_app
from bartender import db

PORT = 80
HOST = "0.0.0.0"
app = create_app()

if __name__ == "__main__":
    db.create_all(app=create_app())
    app.run(host=HOST, port=PORT, debug=True)
