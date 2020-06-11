"""Server for recipe website."""

#json for users
#json for savedrecipes
from flask import (Flask, render_template, request, flash, session, redirect) 

from model import connect_to_db

from jinja2 import StrictUndefined

import os
import requests

import crud 

from pprint import pformat




app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

API_KEY = os.environ["SPOONACULAR_KEY"]

@app.route('/',methods = ['GET', 'POST'])
def login():
    """View homepage and login."""
    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return render_template('homepage.html')

@app.route('/search-results', methods=['GET']) 
def get_ingredient_and_time():
    input_ingredient = request.args.get('ingredient')
    print(input_ingredient)
    input_time = request.args.get('time')
    int_input_time = int(input_time)
    print(int_input_time)

    url = 'https://api.spoonacular.com/recipes'


    # payload = {'query': input_ingredient,
    #             'readyInMinutes': int_input_time,
    #             'number': 10,
    #             'apiKey': API_KEY}

    payload1 = {'query': input_ingredient,
                'maxReadyTime': int_input_time,
                'number': 10,
                'apiKey': API_KEY}

    response1 = requests.get(url + '/complexSearch', params=payload1)

    data1 = response1.json()

    complex_search_results = data1["results"]

    for complex_result in complex_search_results:
        print(complex_result)
        recipe_title = complex_result['title'] 
        print(recipe_title)
        image = complex_result['image'] 
        print(image)
        recipe_id = complex_result['id'] 
        print(recipe_id)
        print(type(int_input_time)) 
        print(f' Recipe: {recipe_title}.')

    payload2 = {'id' : {id}, 
                'apiKey': API_KEY}

    response2 = requests.get(url + '{id}/information', params=payload2)

    return render_template('search-results.html',
                            pformat=pformat,
                            data1=data1,
                            recipe_title=recipe_title,
                            recipe_id=recipe_id,
                            image=image,
                            input_ingredient=input_ingredient,
                            int_input_time=int_input_time,
                            complex_search_results=complex_search_results)

    # data = response.json()

    # recipe_results = data['results']

    # for result in recipe_results:
    #     ready_in_minutes = result['readyInMinutes']
    #     print(ready_in_minutes) 
    #     recipe_title = result['title'] 
    #     print(recipe_title)
    #     image = result['image'] 
    #     print(image)
    #     recipe_id = result['id'] 
    #     print(recipe_id)
    #     print(type(ready_in_minutes))
    #     print(type(int_input_time)) 
    #     print(f' Recipe: {recipe_title}. Total cooking time = {ready_in_minutes}')

    # recipe = crud.get_recipe_by_id(recipe_id)

    # return render_template('search-results.html',
    #                         pformat=pformat,
    #                         data=data,
    #                         recipe_title=recipe_title,
    #                         recipe_id=recipe_id,
    #                         recipe_results=recipe_results,
    #                         result=result,
    #                         image=image,
    #                         input_ingredient=input_ingredient,
    #                         int_input_time=int_input_time)
#Search Recipes Complex
#Get Recipe Information 

@app.route('/recipes/<recipe_id>')
def recipe_id(recipe_id):
    """Show details on a particular recipe."""
    pass
    # return render_template('recipe_details.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)