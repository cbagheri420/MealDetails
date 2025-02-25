import { useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [food, setFood] = useState('');
  const [nutrition, setNutrition] = useState(null);

  const fetchNutrition = async () => {
    const response = await axios.post('http://127.0.0.1:8000/get-nutrition', { food });
    setNutrition(response.data);
  };

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Meal Planner & Nutrition Analyzer</h1>
      <input type="text" value={food} onChange={(e) => setFood(e.target.value)} placeholder="Enter food" />
      <button onClick={fetchNutrition}>Analyze</button>
      {nutrition && <pre>{JSON.stringify(nutrition, null, 2)}</pre>}
    </div>
  );
}