import os

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

#database setup
app.config["SQLALCHEMY_DATABASE_URI"] = "/Users/andrewroche/Uci_bootcamp_project2/db/seasonal_produce.db"
db = SQLAlchemy(app)



#set homepage to index.html
@app.route("/")
def homepage():
    """Return the homepage."""
    return render_template("index.html")


@app.route('/index.html')
def index():
    """Return the homepage."""
    return render_template('index.html')

@app.route("/vizualizations.html")
def vizualizations():
    """Return the Vizualizations Page."""
    return render_template("vizualizations.html")


@app.route("/contributors.html")
def contributors():
    """Return the Contributors Page."""
    return render_template("contributors.html")






if __name__ == '__main__':
    app.run()
