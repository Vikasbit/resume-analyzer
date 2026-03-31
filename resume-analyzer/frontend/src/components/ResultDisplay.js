import React from 'react';

function ResultDisplay({ result }) {
  if (!result) {
    return null;
  }

  return (
    <div className="results-section">
      <h2>Analysis Results</h2>
      <div className="result-item">
        <strong>Match Score:</strong> {result.match_score}/100
      </div>
      <div className="result-item">
        <strong>Missing Skills:</strong>
        <ul>
          {result.missing_skills.map((skill, index) => (
            <li key={index}>{skill}</li>
          ))}
        </ul>
      </div>
      <div className="result-item">
        <strong>Strengths:</strong>
        <ul>
          {result.strengths.map((strength, index) => (
            <li key={index}>{strength}</li>
          ))}
        </ul>
      </div>
      <div className="result-item">
        <strong>Suggestions:</strong>
        <ul>
          {result.suggestions.map((suggestion, index) => (
            <li key={index}>{suggestion}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ResultDisplay;