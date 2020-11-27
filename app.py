from flask import Flask, render_template
import pymongo

app = Flask(__name__)

#establish connection to MongoDB via pymongo:
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
#create the recipes_db database:
db = client.recipes_db
#create the collections within the recipes_db database:
recipe = db.recipe
main = db.main
side = db.side
dessert = db.dessert
=======
# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.store_inventory
produce = db.produce
>>>>>>> f264b4edbf61b76573d95feb3133bcbcb7b2de51
=======
#establish connection to MongoDB via pymongo:
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
#create the recipes_db database:
db = client.recipes_db
#create the collections within the recipes_db database:
recipe = db.recipe
main = db.main
side = db.side
dessert = db.dessert
>>>>>>> 5ed06c52855d21de9d9c76f64299d252ee6e5d96


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    #foods = list(produce.find())
    #print(foods)

    # render an index.html template and pass it the data you retrieved from the database
    return(

         f"Welcome to the Recipe genrator.<br/>"
        f"Please select from the following:<br/>"
        f"<br/>"
        f"/Dessert.html<br/>"
        f"/Side.html<br/>"
        f"/Main.html<br/>"
    )
    #render_template("index.html", foods=foods)
       


        #display as jsonified dictionary the total precipitation per day for the last year's worth of data
@app.route("/Main")
def main():
    d = 0
    main_list = []
    dictionary_main = {}
    maindishes = list(db.main.find())
    #print(maindishes)
    #return jsonify(maindishes
    #return(main.find_one())
    for dish in maindishes:
#        #print("dish: ", dish["Main"])
       for d in range(0,6):
           results0 =  db.recipe.find({ "Name": {"$regex": dish["Main"][d] }})
           d += 1
           for result in results0:
               dictionary_main["Name"]=result["Name"]
               dictionary_main["url"]=result["url"]
               db.meal2.update_one({'_id': result['_id']}, {'$set': dictionary_main}, upsert=True)
               #main_list.append(dictionary_main)
               #.append({result['Name']}, at {result['url']}") 
               #print(f" You should try {result['Name']}, at {result['url']}")
    recipe = list(db.meal2.find())
    return render_template("Main.html", recipe=recipe)

@app.route("/Dessert.html")
def dessert():
    

    return jsonify()


@app.route("/Side.html")
def side():
    

<<<<<<< HEAD
@app.route("/Main")
def main():
    d = 0
    main_list = []
    dictionary_main = {}
    maindishes = list(db.main.find())
    #print(maindishes)
    #return jsonify(maindishes
    #return(main.find_one())
    for dish in maindishes:
#        #print("dish: ", dish["Main"])
       for d in range(0,6):
           results0 =  db.recipe.find({ "Name": {"$regex": dish["Main"][d] }})
           d += 1
           for result in results0:
               dictionary_main["Name"]=result["Name"]
               dictionary_main["url"]=result["url"]
               db.meal2.update_one({'_id': result['_id']}, {'$set': dictionary_main}, upsert=True)
               #main_list.append(dictionary_main)
               #.append({result['Name']}, at {result['url']}") 
               #print(f" You should try {result['Name']}, at {result['url']}")
    
    return (jsonify(db.meal2.find()))

@app.route("/Main")
def main():
    
    return (jsonify(db.meal2.find()))
    
@app.route("/Main")
def main():
    
    return (jsonify(db.meal2.find()))
=======
    return jsonify()
>>>>>>> f264b4edbf61b76573d95feb3133bcbcb7b2de51

if __name__ == "__main__":
    app.run(debug=True)
