import openai
import json
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_resume(resume_text, job_description):
    """
    Analyze the resume against the job description using OpenAI.

    Args:
        resume_text (str): Text extracted from the resume.
        job_description (str): The job description text.

    Returns:
        dict: Analysis result with match_score, missing_skills, strengths, suggestions.
    """
    prompt = f"""
Compare the resume with the job description and return a JSON object with the following keys:
- match_score: an integer between 0 and 100
- missing_skills: an array of strings listing skills missing from the resume
- strengths: an array of strings listing strengths from the resume
- suggestions: an array of strings with suggestions to improve the resume

Resume:
{resume_text}

Job Description:
{job_description}

Return only the JSON object, no additional text.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.5
        )
        content = response.choices[0].message.content.strip()
        # Parse the JSON response
        result = json.loads(content)
        return result
    except Exception as e:
        # In case of error, return a default response
        return {
            "match_score": 0,
            "missing_skills": ["Error in analysis"],
            "strengths": [],
            "suggestions": ["Please try again"]
        }