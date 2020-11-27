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


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    #foods = list(produce.find())
    #print(foods)

    # render an index.html template and pass it the data you retrieved from the database

    return render_template("index.html")
    
    #(

    #      f"Welcome to the Recipe genrator.<br/>"
    #     f"Please select from the following:<br/>"
    #     f"<br/>"
    #     f"/Dessert<br/>"
    #     f"/Side<br/>"
    #     f"/Main<br/>"
    # )
    #render_template("index.html", foods=foods)
       


        #display as jsonified dictionary the total precipitation per day for the last year's worth of data
@app.route("/Main")
def main():
    d = 0
    main_list = []
    dictionary_main = {}
    maindishes = list(db.main.find())

    for dish in maindishes:

       for d in range(0,6):
           results0 =  db.recipe.find({ "Name": {"$regex": dish["Main"][d] }})
           d += 1
           for result in results0:
               dictionary_main["Name"]=result["Name"]
               dictionary_main["url"]=result["url"]
               db.meal2.update_one({'_id': result['_id']}, {'$set': dictionary_main}, upsert=True)

    recipe = list(db.meal2.find())
    return render_template("Main.html", recipe=recipe)

@app.route("/Dessert")
def dessert():
    ds = 0
    dessert_list = []
    dictionary_dessert = {}
    dessertdishes = list(db.dessert.find())
 
    for dish in dessertdishes:

       for ds in range(0,9):
           results2 =  db.recipe.find({ "Name": {"$regex": dish["Dessert"][ds] }})
           ds += 1
           for result in results2:
               dictionary_dessert["Name"]=result["Name"]
               dictionary_dessert["url"]=result["url"]
               db.tdessert.update_one({'_id': result['_id']}, {'$set': dictionary_dessert}, upsert=True)

    recipe2 = list(db.tdessert.find())
    return render_template("Dessert.html", recipe2=recipe2)

@app.route("/Side")
def side():
    sd = 0
    side_list = []
    dictionary_side = {}
    sidedishes = list(db.side.find())
 
    for dish in sidedishes:

       for sd in range(0,8):
           results3 =  db.recipe.find({ "Name": {"$regex": dish["Side"][sd] }})
           sd += 1
           for result in results3:
               dictionary_side["Name"]=result["Name"]
               dictionary_side["url"]=result["url"]
               db.tside.update_one({'_id': result['_id']}, {'$set': dictionary_side}, upsert=True)

    recipe3 = list(db.tside.find())
    return render_template("Side.html", recipe3=recipe3)    


if __name__ == "__main__":
    app.run(debug=True)
