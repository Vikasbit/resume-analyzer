import React from 'react';
import axios from 'axios';

function AnalyzeButton({ resume, jobDescription, onResult, setLoading }) {
  const handleAnalyze = async () => {
    // Validate inputs
    if (!resume) {
      alert('Please upload a resume.');
      return;
    }
    if (!jobDescription.trim()) {
      alert('Please enter a job description.');
      return;
    }

    setLoading(true);
    onResult(null); // Clear previous results

    // Prepare form data for multipart upload
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('job_description', jobDescription);

    try {
      const response = await axios.post('http://localhost:8000/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      onResult(response.data);
    } catch (error) {
      console.error('Error analyzing resume:', error);
      alert('Error analyzing resume. Please check the console for details.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="analyze-section">
      <button onClick={handleAnalyze} disabled={setLoading}>
        Analyze Resume
      </button>
    </div>
  );
}

export default AnalyzeButton;