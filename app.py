from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import logging
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model
try:
    model = load('model/iris_model.joblib')
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Model loading failed: {str(e)}")
    raise

@app.route('/')
def home():
    return jsonify({
        'status': 'running',
        'message': 'Iris Classifier API',
        'endpoints': {
            '/predict (POST)': 'Predict iris species'
        }
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get and validate input data
        data = request.get_json()
        
        if not data:
            raise ValueError("No input data provided")
            
        required_features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        if not all(feat in data for feat in required_features):
            raise ValueError(f"Required features: {required_features}")
        
        # Prepare features for prediction
        features = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        probabilities = model.predict_proba([features])[0]
        
        return jsonify({
            'success': True,
            'prediction': int(prediction),
            'species': ['setosa', 'versicolor', 'virginica'][prediction],
            'confidence': float(np.max(probabilities)),
            'probabilities': {
                'setosa': float(probabilities[0]),
                'versicolor': float(probabilities[1]),
                'virginica': float(probabilities[2])
            }
        })
        
    except ValueError as e:
        logger.warning(f"Input error: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e),
            'type': 'input_error'
        }), 400
        
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return jsonify({
            'success': False,
            'error': "Prediction failed" if not app.debug else str(e),
            'type': 'server_error'
        }), 500

# Handle 404 errors
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'error': str(e),
        'type': 'not_found'
    }), 404

# Handle all HTTP exceptions
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({
        'success': False,
        'error': str(e.description),
        'type': 'http_error'
    }), e.code
