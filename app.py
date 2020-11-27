from flask import Flask, jsonify

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
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

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

if __name__ == "__main__":
    app.run(debug=True)