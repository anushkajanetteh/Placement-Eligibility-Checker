# Placement Eligibility Checker

Console-based Python project. It reads `jobs.csv` and `students.csv`, extracts job criteria, checks them, matches students locally, and writes four reports.

## Privacy
Only job-post text is sent to the LLM. Student records remain in Python and are never sent to the API. All lists are drafts; a placement officer must verify every list before sharing. Never upload `.env` or an API key to GitHub.

## Setup (Windows / VS Code)
1. Open this folder in VS Code.
2. Terminal > New Terminal.
3. Run `python -m pip install python-dotenv`
4. Optional API setup: copy `.env.example` to `.env` and add your own API key. Keep `.env` private.
5. Run `python main.py`.
6. If no API key exists or the API fails, the code retries once and uses a labelled offline fallback.
7. Open `outputs/` to see `job_summary.csv`, `eligible.csv`, `review.csv`, and `summary.txt`.

## Tests
Run `python tests/eval_harness.py` and `python tests/red_team_tests.py`.

## Suggested Git commits
1. Add specification and sample CSV inputs.
2. Implement extraction, validation and matching.
3. Add reports and evaluation/red-team tests.
4. Complete documentation.
