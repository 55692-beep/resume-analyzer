from flask import Flask, render_template, request
from resume_parser import extract_text_from_pdf
from job_matcher import match_resume_to_job
from skills import extract_skills, get_missing_skills

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    skills = []
    missing_skills = []

    if request.method == 'POST':
        file = request.files['resume']
        job_desc = request.form['job_description']

        if file:
            resume_text = extract_text_from_pdf(file)

            score = match_resume_to_job(resume_text, job_desc)

            skills = extract_skills(resume_text)
            missing_skills = get_missing_skills(skills, job_desc)

    return render_template(
        'index.html',
        score=score,
        skills=skills,
        missing_skills=missing_skills
    )

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)