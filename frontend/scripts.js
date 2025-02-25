async function getNutrition() {
    const food = document.getElementById('foodInput').value;

    if (!food) {
        alert("Please enter a food item.");
        return;
    }

    const response = await fetch('http://127.0.0.1:8000/get-nutrition', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ food })
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('result').innerHTML = JSON.stringify(data, null, 2);
    } else {
        document.getElementById('result').innerHTML = "Error fetching nutrition data.";
    }
}