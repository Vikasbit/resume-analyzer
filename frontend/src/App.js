import React, { useState } from 'react';
import UploadResume from './components/UploadResume';
import JobDescriptionInput from './components/JobDescriptionInput';
import AnalyzeButton from './components/AnalyzeButton';
import ResultDisplay from './components/ResultDisplay';
import './App.css';

function App() {
  // State for the uploaded resume file
  const [resume, setResume] = useState(null);
  // State for the job description text
  const [jobDescription, setJobDescription] = useState('');
  // State for the analysis result
  const [result, setResult] = useState(null);
  // State for loading indicator
  const [loading, setLoading] = useState(false);

  return (
    <div className="App">
      <h1>AI Resume Analyzer</h1>
      <UploadResume onFileSelect={setResume} />
      <JobDescriptionInput value={jobDescription} onChange={setJobDescription} />
      <AnalyzeButton
        resume={resume}
        jobDescription={jobDescription}
        onResult={setResult}
        setLoading={setLoading}
      />
      {loading && <p>Analyzing your resume...</p>}
      <ResultDisplay result={result} />
    </div>
  );
}

export default App;