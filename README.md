# Iris_Data-Model-
  # **Iris Dataset - Model Training**  
This project demonstrates how to load the Iris dataset, preprocess it, and train a machine learning model for classification.  

---

## **Dataset Description**  
The **Iris dataset** contains measurements of 150 iris flowers from three species:  
- **Setosa** (0)  
- **Versicolor** (1)  
- **Virginica** (2)  

Each sample has four features:  
1. Sepal length (cm)  
2. Sepal width (cm)  
3. Petal length (cm)  
4. Petal width (cm)  

---

## **Steps to Run the Model**  

### **1. Install Required Libraries**  
```bash
pip install pandas scikit-learn
```

### **2. Load the Dataset**  
You can load the dataset directly from `scikit-learn`:  

```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
X = iris.data  # Features
y = iris.target  # Labels
```

Alternatively, if you have a CSV file (`iris.csv`):  
```python
df = pd.read_csv('iris.csv')
X = df.drop('species', axis=1)  # Features
y = df['species']  # Target
```

### **3. Split Data into Training & Testing Sets**  
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### **4. Train a Model (Example: Random Forest Classifier)**  
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

### **5. Evaluate the Model**  
```python
from sklearn.metrics import accuracy_score, classification_report

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

### **6. Save the Model (Optional)**  
```python
import joblib

joblib.dump(model, 'iris_model.pkl')  # Save model
```

### **7. Load & Use the Model for Predictions**  
```python
loaded_model = joblib.load('iris_model.pkl')
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Example input
prediction = loaded_model.predict(new_data)
print("Predicted class:", iris.target_names[prediction][0])
```

---

## **Expected Output**  
- **Accuracy**: ~96-100% (since Iris is an easy dataset)  
- **Classification Report**: Shows precision, recall, and F1-score for each class.  

---

## **License**  
This project is open-source under the **MIT License**.  

---

### **Further Improvements**  
- Try different models (SVM, Logistic Regression, Neural Networks).  
- Perform hyperparameter tuning with `GridSearchCV`.  
- Deploy the model using Flask/FastAPI for web inference.  

