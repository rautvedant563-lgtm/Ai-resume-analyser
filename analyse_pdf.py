from google import genai
import os

def analyse_resume_gemini(resume_text, job_description):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "Error: GEMINI_API_KEY not found in .env file."

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert resume reviewer. Compare the resume below with the job description
and give a detailed analysis including:
1. Match score (out of 100)
2. Key strengths
3. Missing skills/keywords
4. Suggestions to improve the resume

Resume:
{resume_text}

Job Description:
{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text