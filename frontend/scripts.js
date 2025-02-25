async function getNutrition() {
    const food = document.getElementById('foodInput').value;
    const resultDiv = document.getElementById('nutritionResult');

    if (!food) {
        resultDiv.innerHTML = "Please enter a food item.";
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:8000/get-nutrition', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ food })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.innerHTML = JSON.stringify(data, null, 2);
        } else {
            resultDiv.innerHTML = `Error: ${data.detail}`;
        }
    } catch (error) {
        resultDiv.innerHTML = "Error calling the API.";
    }
}