import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://backend-service:5000/api/message')
      .then(response => setMessage(response.data.message))
      .catch(() => setMessage('Error fetching message'));
  }, []);

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: 20 }}>
      <h1>Frontend - React App</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}

export default App;
