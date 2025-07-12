from flask import Flask, jsonify, request, render_template
from joblib import load
import numpy as np
import logging
from werkzeug.exceptions import HTTPException

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['JSON_SORT_KEYS'] = False
    
    # Logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Load model
    try:
        app.model = load('model/iris_model.joblib')
        logger.info("Model loaded successfully")
    except Exception as e:
        logger.error(f"Model loading failed: {str(e)}")
        raise
    
    # Routes
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/predict', methods=['POST'])
    def predict():
        try:
            data = request.get_json()
            required = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
            
            if not all(k in data for k in required):
                raise ValueError(f"Missing required fields: {required}")
                
            features = [
                float(data['sepal_length']),
                float(data['sepal_width']),
                float(data['petal_length']),
                float(data['petal_width'])
            ]
            
            prediction = app.model.predict([features])[0]
            proba = app.model.predict_proba([features])[0]
            
            return jsonify({
                'success': True,
                'prediction': int(prediction),
                'species': ['setosa', 'versicolor', 'virginica'][prediction],
                'confidence': float(np.max(proba)),
                'probabilities': {
                    'setosa': float(proba[0]),
                    'versicolor': float(proba[1]),
                    'virginica': float(proba[2])
                }
            })
            
        except ValueError as e:
            return jsonify({'success': False, 'error': str(e)}), 400
        except Exception as e:
            logger.error(str(e))
            return jsonify({'success': False, 'error': "Prediction failed"}), 500
    
    return app

# Instantiate the app
app = create_app()
