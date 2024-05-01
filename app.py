import os, random

from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    {"id": 1, "quote": "Quote 1", "author": "Author 1"},
    {"id": 2, "quote": "Quote 2", "author": "Author 2"}
]

@app.route('/')
def index():
    return "Welcome to the Random Quote API!"

@app.route('/quote')
def get_quote():
    return jsonify(random.choice(quotes))

if __name__ == '__main__':
   app.run()
