import React, { useRef, useState } from 'react';

function App() {
  const videoRef = useRef(null);
  const [prediction, setPrediction] = useState('');

  const captureAndPredict = async () => {
    const canvas = document.createElement('canvas');
    canvas.width = 64;
    canvas.height = 64;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(videoRef.current, 0, 0, 64, 64);
    const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg'));
    
    const formData = new FormData();
    formData.append('image', blob);

    const res = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    setPrediction(data.prediction);
  }

  return (
    <div>
      <h1>SignLang Real-Time Recognition</h1>
      <video ref={videoRef} autoPlay width="300" height="300" />
      <button onClick={captureAndPredict}>Predict</button>
      <h2>Prediction: {prediction}</h2>
    </div>
  );
}

export default App;
