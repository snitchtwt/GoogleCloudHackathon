import nltk
import random
import string
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

df = pd.read_csv('diet_plans.csv')
df['plan'] = df['plan'].str.lower()

# Define the vectorizer and similarity function
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
similarity = cosine_similarity
def get_closest_plan(query):
    query = query.lower()
    query_vec = vectorizer.fit_transform([query])
    similarities = similarity(query_vec, vectorizer.transform(df['plan'])).flatten()
    closest_idx = np.argmax(similarities)
    return df.iloc[closest_idx]['plan'], df.iloc[closest_idx]['macros'], df.iloc[closest_idx]['calories']


def chatbot():
    print("Welcome to the Diet Plan Chatbot!")
    print("Ask me for a diet plan and I'll provide you with the macros and calories.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for exit condition
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Get closest plan from dataset
        closest_plan, macros, calories = get_closest_plan(user_input)
        
        # Print the result
        print("Chatbot: Here's the closest diet plan I found:")
        print("Plan: {}".format(closest_plan))
        print("Macros: {}".format(macros))
        print("Calories: {}".format(calories))


def chatbot():
    # ...

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for exit condition
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Get closest plan from dataset
        try:
            closest_plan, macros, calories = get_closest_plan(user_input)
        except ValueError:
            print("Chatbot: Sorry, I couldn't find a diet plan that matches your query. Please try again.")
            continue
        
        # Print the result
        print("Chatbot: Here's the closest diet plan I found:")
        print("Plan: {}".format(closest_plan))
        print("Macros: {}".format(macros))
        print("Calories: {}".format(calories))


def chatbot():
    # ...

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for exit condition
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Get closest plan from dataset
        try:
            closest_plan, macros, calories, meal_timings, portion_sizes, food_recommendations = get_closest_plan(user_input)
        except ValueError:
            print("Chatbot: Sorry, I couldn't find a diet plan that matches your query. Please try again.")
            continue
        
        # Print the result
        print("Chatbot: Here's the closest diet plan I found:")
        print("Plan: {}".format(closest_plan))
        print("Macros: {}".format(macros))
        print("Calories: {}".format(calories))
        
        # Print additional information if requested
        if 'meal timings' in user_input:
            print("Meal Timings: {}".format(meal_timings))
        if 'portion sizes' in user_input:
            print("Portion Sizes: {}".format(portion_sizes))
        if 'food recommendations' in user_input:
            print("Food Recommendations: {}".format(food_recommendations))
def get_personalized_plan(age, weight, height, activity_level):
    # Calculate basal metabolic rate (BMR)
    if activity_level == 'sedentary':
        activity_factor = 1.2
    elif activity_level == 'lightly active':
        activity_factor = 1.375
    elif activity_level == 'moderately active':
        activity_factor = 1.55
    elif activity_level == 'very active':
        activity_factor = 1.725
    else:
        raise ValueError("Invalid activity level.")
    
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    
    # Calculate daily calorie needs
    daily_calories = int(bmr * activity_factor)
    
    # Calculate macro needs
    protein = int(weight * 1.5)
    fat = int(daily_calories * 0.3 / 9)
    carbs = int((daily_calories - protein * 4 - fat * 9) / 4)
    
    # Return personalized plan
    return "Personalized Plan", (protein, carbs, fat), daily_calories


def chatbot():
    # ...

    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check for exit condition
        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Check for personalized plan request
        if 'personalized plan' in user_input:
            # Get personal information from user
            age = int(input("What is your age? "))
            weight = int(input("What is your weight in kg? "))
            height = int(input("What is your height in cm? "))
            activity_level = input("What is your activity level? (sedentary, lightly active, moderately active, very active) ")
            
            # Calculate personalized plan
            closest_plan, macros, calories = get_personalized_plan(age, weight, height, activity_level)
            
            # Print the result
            print("Chatbot: Here's your personalized diet plan:")
            print("Plan: {}".format(closest_plan))
            print("Macros: {}".format(macros))
            print("Calories: {}".format(calories))
        else:
            # Get closest plan from dataset
            try:
                closest_plan, macros, calories, meal_timings, portion_sizes, food_recommendations = get_closest_plan(user_input)
            except ValueError:
                print("Chatbot: Sorry, I couldn't find a diet plan that matches your query. Please try again.")
                continue
            
            # Print the result
            print("Chatbot: Here's the closest diet plan I found:")
            print("Plan: {}".format(closest_plan))
            print("Macros: {}".format(macros))
            print("Calories: {}".format(calories))
            
            # Print additional information if requested
            if 'meal timings' in user_input:
                print("Meal Timings: {}".format(meal_timings))
            if 'portion sizes' in user_input:
                print("Portion Sizes: {}".format(portion_sizes))
            if 'food recommendations' in user_input:
                print("Food Recommendations: {}".format(food_recommendations))
