import React from 'react';

const ResultsDisplay = ({ results }) => {
  if (results.error) {
    return (
      <div className="error">
        <h3>Error</h3>
        <p>{results.error}</p>
      </div>
    );
  }

  const { present_students, absent_students, total_faces_detected, total_students } = results;

  return (
    <div className="results">
      <div className="stats">
        <div className="stat-item">
          <div className="stat-number">{present_students.length}</div>
          <div>Present</div>
        </div>
        <div className="stat-item">
          <div className="stat-number">{absent_students.length}</div>
          <div>Absent</div>
        </div>
        <div className="stat-item">
          <div className="stat-number">{total_faces_detected}</div>
          <div>Faces Detected</div>
        </div>
        <div className="stat-item">
          <div className="stat-number">{total_students}</div>
          <div>Total Students</div>
        </div>
      </div>

      <div className="students-grid">
        <div className="student-list present">
          <h3>Present Students ({present_students.length})</h3>
          {present_students.length === 0 ? (
            <p>No students detected as present</p>
          ) : (
            present_students.map((student, index) => (
              <div key={index} className="student-item">
                <span>{student.name}</span>
                <span>{student.roll_number}</span>
              </div>
            ))
          )}
        </div>

        <div className="student-list absent">
          <h3>Absent Students ({absent_students.length})</h3>
          {absent_students.length === 0 ? (
            <p>All students are present!</p>
          ) : (
            absent_students.map((student, index) => (
              <div key={index} className="student-item">
                <span>{student.name}</span>
                <span>{student.roll_number}</span>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default ResultsDisplay;