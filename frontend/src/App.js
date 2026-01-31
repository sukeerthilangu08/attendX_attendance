import React, { useState } from 'react';
import './App.css';
import AttendanceForm from './components/AttendanceForm';
import ResultsDisplay from './components/ResultsDisplay';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="App">
      <div className="header">
        <h1>AttendX - Automated Attendance System</h1>
        <p>Upload a group photo to automatically take attendance using face recognition</p>
      </div>

      <AttendanceForm 
        onResults={setResults} 
        onLoading={setLoading}
      />

      {loading && (
        <div className="loading">
          <h3>Processing attendance...</h3>
          <p>Analyzing faces and matching with student database...</p>
        </div>
      )}

      {results && !loading && (
        <ResultsDisplay results={results} />
      )}
    </div>
  );
}

export default App;