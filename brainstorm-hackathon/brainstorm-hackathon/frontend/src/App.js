import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

function App() {
  const [plotData, setPlotData] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/generate_plot')
      .then(response => {
        setPlotData(response.data.plot);
      })
      .catch(error => console.error('Error fetching plot:', error));
  }, []);

  return (
    <div className="App">
      <h1>Brainstorm Neuroscience Hackathon</h1>
      {plotData && (
        <img src={} alt="Neuroscience Plot" />
      )}
    </div>
  );
}

export default App;
