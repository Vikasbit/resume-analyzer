import React from 'react';

function UploadResume({ onFileSelect }) {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      onFileSelect(file);
    } else {
      alert('Please select a PDF file.');
    }
  };

  return (
    <div className="upload-section">
      <label htmlFor="resume-upload">Upload Resume (PDF):</label>
      <input
        id="resume-upload"
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
      />
    </div>
  );
}

export default UploadResume;