from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('model/iris_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
        pred = model.predict([features])[0]
        species = ['setosa', 'versicolor', 'virginica'][pred]
        return jsonify({
            'success': True,
            'prediction': species,
            'image_url': f'/static/images/{species}.jpg'  # Add species images
        })
    except Exception as e:from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)
model = load('iris_model.joblib')  # Your trained model

# Free-to-use image URLs from Wikimedia Commons
IMAGE_MAP = {
    'setosa': 'https://upload.wikimedia.org/wikipedia/commons/1/11/Iris_setosa_3.jpg',
    'versicolor': 'https://upload.wikimedia.org/wikipedia/commons/3/3e/Iris_versicolor_3.jpg',
    'virginica': 'https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
        pred = model.predict([features])[0]
        species = ['setosa', 'versicolor', 'virginica'][pred]
        
        return jsonify({
            'success': True,
            'prediction': species,
            'image_url': IMAGE_MAP[species],
            'fun_fact': get_fun_fact(species)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def get_fun_fact(species):
    facts = {
        'setosa': 'Known as the "Arctic Iris", it grows in cold climates',
        'versicolor': 'Also called "Harlequin Blueflag", blooms in late spring',
        'virginica': 'Native to eastern North America, prefers wetlands'
    }
    return facts.get(species, '')

if __name__ == '__main__':
    app.run(debug=True)
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)