import spacy

nlp = spacy.load("en_core_web_sm")

# Simple skill database (you can expand later)
SKILLS_DB = [
    "python", "java", "c++", "sql", "flask", "django",
    "machine learning", "deep learning", "nlp",
    "html", "css", "javascript", "react",
    "data analysis", "pandas", "numpy"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
def get_missing_skills(resume_skills, job_description):
    job_description = job_description.lower()

    missing = []

    for skill in SKILLS_DB:
        if skill in job_description and skill not in resume_skills:
            missing.append(skill)

    return missing