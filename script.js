document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Show loading spinner
    const spinner = document.getElementById('spinner');
    spinner.classList.remove('d-none');
    
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                sepal_length: document.getElementById('sepal_length').value,
                sepal_width: document.getElementById('sepal_width').value,
                petal_length: document.getElementById('petal_length').value,
                petal_width: document.getElementById('petal_width').value
            })
        });

        const data = await response.json();
        
        if (data.success) {
            // Display results
            document.getElementById('predictionResult').textContent = data.prediction;
            document.getElementById('flowerImage').src = data.image_url;
            document.getElementById('funFact').textContent = data.fun_fact;
            
            // Switch views
            document.getElementById('result').classList.remove('d-none');
            document.getElementById('predictionForm').classList.add('d-none');
            
            // Smooth scroll to results
            document.getElementById('result').scrollIntoView({ behavior: 'smooth' });
        } else {
            alert(`Error: ${data.error}`);
        }
    } catch (error) {
        alert('Failed to connect to server');
    } finally {
        spinner.classList.add('d-none');
    }
});

// Reset button
document.getElementById('resetBtn').addEventListener('click', () => {
    document.getElementById('predictionForm').reset();
    document.getElementById('result').classList.add('d-none');
    document.getElementById('predictionForm').classList.remove('d-none');
    window.scrollTo({ top: 0, behavior: 'smooth' });
});