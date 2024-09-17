from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '47d89e1c6e7a4d908f47327c49d7bfeb'  # Замените на Ваш API ключ OpenWeatherMap
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = 'Vladimir'

    response = requests.get(BASE_URL, params={
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Для получения температуры в Цельсиях
    })

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data['name'],
            "temperature": data['main']['temp'],
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "City not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0')
