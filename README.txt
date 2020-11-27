ETL Project

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

