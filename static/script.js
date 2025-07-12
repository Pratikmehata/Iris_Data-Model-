document.getElementById('irisForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const btn = e.target.querySelector('button');
    btn.disabled = true;
    btn.textContent = 'Predicting...';
    
    try {
        const data = {
            sepal_length: document.getElementById('sepal_length').value,
            sepal_width: document.getElementById('sepal_width').value,
            petal_length: document.getElementById('petal_length').value,
            petal_width: document.getElementById('petal_width').value
        };

        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        if (result.success) {
            document.getElementById('prediction').textContent = result.species;
            document.getElementById('confidence').textContent = (result.confidence * 100).toFixed(1);
            document.querySelector('.confidence-level').style.width = `${result.confidence * 100}%`;
            document.getElementById('result').classList.remove('hidden');
        } else {
            alert(`Error: ${result.error}`);
        }
    } catch (error) {
        alert('Failed to connect to server');
    } finally {
        btn.disabled = false;
        btn.textContent = 'Predict Species';
    }
});

document.getElementById('resetBtn').addEventListener('click', () => {
    document.getElementById('irisForm').reset();
    document.getElementById('result').classList.add('hidden');
});