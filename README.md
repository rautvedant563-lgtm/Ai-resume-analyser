# Ai-resume-analyse

An AI-powered tool that analyzes resumes against job descriptions using Google's Gemini API. It parses resume PDFs, compares them to a given job description, and returns insights to help improve resume-job fit.

## Features

- 📄 Extracts and reads content from resume PDFs
- 🤖 Uses Google Gemini (`gemini-2.0-flash`) to analyze resume content against a job description
- 🔍 Provides feedback on how well a resume matches a given role
- 🖥️ Simple web interface (HTML) for interacting with the tool

## Tech Stack

- **Python** — core application logic
- **Google Gemini API** (`google-genai`) — AI-powered resume analysis
- **HTML** — front-end interface
- **python-dotenv** — environment variable management

## Project Structure

```
ai-analyzer/
├── main.py            # Entry point — runs the resume analysis flow
├── analyse_pdf.py     # Handles PDF parsing and Gemini API calls
├── index.html          # Web interface
├── .env                # API keys and environment variables (not committed)
└── requirements.txt    # Python dependencies
```

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/ai-analyzer.git
   cd ai-analyzer
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Gemini API key to a `.env` file
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the analyzer
   ```bash
   python main.py
   ```

## Usage

Provide a resume (PDF) and a job description as input. The tool extracts the resume content, sends it along with the job description to Gemini, and returns an analysis of how well the resume aligns with the role — including strengths, gaps, and suggestions for improvement.

## Roadmap

- [ ] Improve error handling for API failures
- [ ] Add support for multiple resume formats (DOCX, TXT)
- [ ] Enhance web UI with real-time feedback
- [ ] Add scoring system for resume-job match



## Author

Vedant — B.Tech CSE student, RTMNU Nagpur
