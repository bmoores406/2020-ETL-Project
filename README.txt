ETL-project
Extract
We used 2 different datasets from the public platforms Kaggle and DataWorld which lead us to a survey for Thanksgiving and Christmas Recipes. The data in the two files included the following information:
	• Recipe Title
	• Recipe Description
	• Recipe Author
	• Ingredients list
	• Step by step method
	
The fields of interest include the following:
	• What is typically the main dish at your Thanksgiving dinner?
	• Name
	• URL
	• Ingredients
	• Which of these side dishes are typically served at your Thanksgiving dinner?
	• Which type of pie is typically served at your Thanksgiving dinner?

<<<<<<< HEAD
Group Members - Greg Dorleus, Josh Cohn, Brian Moores

Extract

Data

Christmas Recipes
This JSON lines file contains 1600 christmas cooking recipes scraped from BBC Good Food.

Thanksgiving 2015
Using a SurveyMonkey poll, we asked 1,058 respondents on Nov. 17, 2015 the following questions about their Thanksgiving:
What is typically the main dish at your Thanksgiving dinner?
Which of these side dishes are typically served at your Thanksgiving dinner? Please select all that apply.
Which of these desserts do you typically have at Thanksgiving dinner? Please select all that apply.

We used pandas to view and clean our Thankgiving Dinner Survey CSV and our Holiday Recipes API.  

Transform 

For the Survey we had to rename columns and break them down into three categories: Main Dishes, Side Dishes, and Desserts.
We transposed and indexed each dataframe to get a list of unique dishes for each category, 
then we converted each list into a dictionary for Main Dishes, Side Dishes, and Desserts.

We connected to MongoDB and created a Recipes_DB in which we created collections Main Dishes, Side Dishes, and Desserts.
Then 

Load

=======
The following sources for our datasets used:
https://data.world/fivethirtyeight/thanksgiving-2015
https://www.kaggle.com/gjbroughton/christmas-recipesTransformation
Transformation
In order to transform the public data and use it in our study we performed the following:
	• We used Pandas functions in Jupyter Notebook to load all the CSV and JSON files.
	• Reviewed the files and transformed into data frames
	• There were roughly 2,000 values 
	• Create a new collection
	• Kept the recipes and show your meals (main dish, side dish, desserts)
	• Each of the categories will have their own collection after running
	• Each app creates its own collection within the recipes database so you have the filtered nd unfiltered
		○ For the app we use flask stuff app.py
	
	• Created a Flask app with 3 pathways pie, main, side dish
	• Queried to go through the dictionary of our categories
	

Load
The last step was to transfer our final output into a Mongo Database. We created a database and respective key words to match the ingredients from the final Panda's Data Frame using MongoDB to store our original clean data sets. We reconnected to the database and generated additional queries for the data frames.
Summary
There were some limitations to our findings due to the data available. However, we were able to create our app in our initial project proposal listed in the ETL Project Final Write up.
>>>>>>> f264b4edbf61b76573d95feb3133bcbcb7b2de51
