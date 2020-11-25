from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

if __name__ == "__main__":
    app.run(debug=True)