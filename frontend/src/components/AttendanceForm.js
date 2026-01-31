import React, { useState } from 'react';
import axios from 'axios';

const AttendanceForm = ({ onResults, onLoading }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => setPreview(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  const handleTakeAttendance = async () => {
    if (!selectedFile) {
      alert('Please select an image first');
      return;
    }

    onLoading(true);
    
    const formData = new FormData();
    formData.append('image', selectedFile);

    try {
      const response = await axios.post('/api/take-attendance', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      
      onResults(response.data.data);
    } catch (error) {
      console.error('Error taking attendance:', error);
      onResults({ error: error.response?.data?.error || 'Failed to process attendance' });
    } finally {
      onLoading(false);
    }
  };

  return (
    <div className="upload-section">
      <h2>Upload Group Photo</h2>
      <div className="file-input">
        <input
          type="file"
          accept="image/*"
          onChange={handleFileSelect}
          id="imageInput"
        />
        <label htmlFor="imageInput">
          {selectedFile ? selectedFile.name : 'Choose classroom photo...'}
        </label>
      </div>
      
      {preview && (
        <div style={{ margin: '20px 0' }}>
          <img 
            src={preview} 
            alt="Preview" 
            style={{ maxWidth: '300px', maxHeight: '200px', borderRadius: '5px' }}
          />
        </div>
      )}
      
      <button 
        className="btn btn-primary" 
        onClick={handleTakeAttendance}
        disabled={!selectedFile}
      >
        Take Attendance
      </button>
    </div>
  );
};

export default AttendanceForm;