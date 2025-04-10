import argparse
import os
import pandas as pd
from agents.cv_parser import extract_text_from_pdf
from agents.jd_summarizer import summarize_job_descriptions
from agents.matcher import calculate_match_score
from agents.interview_inviter import generate_invite
from tools.db_handler import store_candidate_result

def main(jd_csv_path: str, resume_dir: str, threshold: int = 75):
    jd_summary = summarize_job_descriptions(jd_csv_path)
    print("\n[✓] Job Description Summarized.")

    for file in os.listdir(resume_dir):
        if not file.endswith(".pdf"):
            continue
        resume_path = os.path.join(resume_dir, file)
        print(f"\nProcessing {file}...")

        cv_text = extract_text_from_pdf(resume_path)
        if not cv_text.strip():
            print(f"Skipping {file} due to empty content.")
            continue

        result = calculate_match_score(jd_summary, cv_text)
        print(f"Match Score: {result['score']} - Reason: {result['reason']}")

        if result['score'] >= threshold:
            invite = generate_invite(jd_summary, cv_text)
            print(f"\n[✓] Candidate Shortlisted.\nGenerated Interview Invite:\n{invite}\n")

            store_candidate_result(file, result['score'], result['reason'], invite)
        else:
            print("Candidate not shortlisted.\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Job Screening CLI")
    parser.add_argument("--jd", type=str, required=True, help="Path to job_description.csv")
    parser.add_argument("--resumes", type=str, required=True, help="Folder containing PDF resumes")
    parser.add_argument("--threshold", type=int, default=75, help="Match threshold (default=75)")
    args = parser.parse_args()

    main(args.jd, args.resumes, args.threshold)
