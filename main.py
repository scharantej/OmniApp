
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    api_key = 'YOUR_API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    weather = request.args.get('weather')
    api_key = 'YOUR_API_KEY'
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}&weather={weather}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
