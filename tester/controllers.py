# app is instanced in __init__.py; this gets it from there
from . import app
from flask import abort, request, redirect, make_response, flash, session, render_template
import json

@app.route("/")
def index():
    return render_template("layout.html")