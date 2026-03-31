import React from 'react';

function JobDescriptionInput({ value, onChange }) {
  return (
    <div className="job-description-section">
      <label htmlFor="job-description">Job Description:</label>
      <textarea
        id="job-description"
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Paste the job description here..."
        rows={10}
        cols={50}
      />
    </div>
  );
}

export default JobDescriptionInput;