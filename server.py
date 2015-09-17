import random

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    """Show our index page."""

    return render_template("index.html")


@app.route('/ajax-call')
def call_ajax():
    """Render page 1"""
    
    return "YAY"




if __name__ == "__main__":
    app.run(debug=True)