# 🧠 JobGenie

**JobGenie** is a local LLM‑powered Python application that acts like an Applicant Tracking System (ATS). It lets recruiters:

* Import a `.csv` containing job descriptions
* Analyze candidate resumes
* Shortlist candidates based on their match to roles
* Automate & personalize email outreach to shortlisted applicants

---

## ✨ Features

### 1. Job Description Parsing

* Reads and processes job descriptions exported as `.csv`.
* Uses a local LLM to extract key skills, responsibilities, qualifications, and other relevant attributes.

### 2. Resume Analysis

* Scans resume documents (`.pdf files`).
* Converts each resume into structured, machine-readable form.
* Evaluates relevance against each job description by scoring how well candidates match required skills and experiences.

### 3. Candidate Shortlisting

* Automatically ranks candidates for each open position.
* Supports customizable thresholds, letting users manually fine-tune what "shortlist" means.

### 4. Email Automation

* Generates personalized email content for each shortlisted candidate (e.g., “Hi {{Name}}, we reviewed your experience in {{Skill}}...").
* Supports bulk export of emails ready for your mail system or SMTP tunneling.

---

## 🛠️ Getting Started

### Requirements

* Python 3.10+
* Ollama based LocalLLM (llama3 recommended)
* Basic CSV (jobs) and resume files

### Installation

```bash
git clone https://github.com/Yuvraj960/JobGenie.git
cd JobGenie
python3 -m venv venv
source venv/bin/activate         # or venv\Scripts\activate on Windows
pip install -r requirements.txt  # includes langchain, pandas, etc.
```

### Configuration

1. Place your job description CSV (e.g., `jobs.csv`) in the project root.
2. Create a `resumes/` folder and drop in resumes (`.pdf`, `.docx`, `.txt`).


### Usage

```bash
python main.py
```

This script outputs `shortlisted.db` which will store the result of the Shortlisted Candidates.

---

## 📂 Project Structure

```
JobGenie/
├── README.md
├── LICENSE
├── requirements.txt
├── main.py
├── .gitignore
├── Demo.mp4
├── JobGenie.pptx
├── shortlisted.db
├── job_description.csv
│
├── agents/
│   ├── cv_parser.py
│   ├── interview_inviter.py
│   ├── jd_summarizer.py
│   ├── matcher.py
│
├── tools/
│   ├── db_handler.py
│   ├── ollama_handler.py
│
├── sample_data/resumes
│   ├── resume1.pdf
│   ├── resume2.pdf
│   ├── resume3.pdf
│   ├── resume4.pdf

```

---

## 📈 How It Works

1. **parse job CSV** → extract core requirements.
2. **analyze each resume**:

   * extract skills & experience,
   * compute similarity score with job requirements.
3. **shortlist candidates** whose score is above a set threshold.
4. **generate personalized emails**, including name and job-specific highlights.

---

## 🧩 Contribution Guidelines

We welcome your help! Here’s how to get involved:

1. **Fork** the repo.
2. Create a branch: `feature/YourFeatureName`.
3. **Modify** or extend functionality (e.g., add new LLM support, enhance scoring).
4. **Test** thoroughly (`pytest` preferred).
5. Submit a **Pull Request** with detailed description and rationale.

**Contribution ideas:**

* LLM abstraction: support more backends (e.g., Vicuna, Mistral).
* UI layer: build a simple web or CLI dashboard.
* Data export: integrate with Google Sheets, Airtable.
* Quality improvements: handle various resume formats, add multilingual support.
* Logging & monitoring: export usage metrics, track recruiting KPIs.

---

## 🧪 Testing

* Unit tests: `pytest tests/`
* Sample data included: `tests/sample_jobs.csv`, `tests/sample_resumes/`.
* Coverage checks are recommended before merging.

---

## 🚀 Roadmap

* ✅ CSV job upload
* ✅ Resume parsing and scoring
* ✅ Personalized email generation
* 🐞 CLI for end-to-end automation
* 🌐 Web UI dashboard
* 📊 Reporting & analytics module

---

## ✅ License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📫 Contact & Support

* Created by **Yuvraj** — feel free to open issues or PRs!
* GitHub: [Yuvraj960](https://github.com/Yuvraj960)

---

Give **JobGenie** a spin and let AI help streamline your hiring! 🎯

---

Feel free to customize sections such as email templates, configuration details, or testing instructions to match your actual project setup.
