from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.store_inventory
produce = db.produce


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    foods = list(produce.find())
    print(foods)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", foods=foods)
f"Welcome to the Recipe genrator.<br/>"
        f"Please select from the following:<br/>"
        f"<br/>"
        f"/Dessert.html<br/>"
        f"/Side.html<br/>"
        f"/Main.html<br/>"


        #display as jsonified dictionary the total precipitation per day for the last year's worth of data
@app.route("/Main.html")
def main():

    session = Session(engine)

    

    session.close()
    


    return jsonify()

@app.route("/Dessert.html")
def dessert():
    

    return jsonify()


@app.route("/Side.html")
def side():
    

    return jsonify()

if __name__ == "__main__":
    app.run(debug=True)
