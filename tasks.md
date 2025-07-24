# Task List

## ✅ Task 1: Environment Setup
- Clone this repo.
- Configure your Git user: `git config user.name "Your Name"` and `git config user.email "you@example.com"`.
- Commit to `main` after verifying setup.

## ✅ Task 2: Add Basic Log Parsing Script (Bash)
- Inspect `support-ticket-logs/ticket_001.log`.
- Write `scripts/parse_errors.sh` that prints all lines containing "ERROR".
- Script should accept a filename argument.
- Commit in branch: `task/parse-errors`.

## ✅ Task 3: Enhance Parser with Counts
- Update script to output a count of ERROR, WARN, INFO lines.
- Commit and open a pull request (if using GitHub).

## ✅ Task 4: Python JSON Reader
- Use `data/sample.json`.
- Write `scripts/read_json.py` that prints `customer_id`, `environment`, and `error_count`.
- Branch: `task/read-json`.

## ✅ Task 5: Simulate a Merge Conflict
- In branch A, edit `tasks.md` (add a bullet under Task 6).
- In branch B, edit the same section differently.
- Merge B into A (or vice versa) and resolve conflict.
- Keep both edits in final resolution & add a note in commit message.

## ✅ Task 6: Release Tag
- Once Tasks 1–5 are complete, merge to `main`.
- Add a summary to README.md ("Phase 1 complete").
- Tag: `v0.1`.

## Task 7: Advanced Log Analytics
- Create a new Python script `scripts/advanced_log_analyzer.py`
- Add functionality to:
  - Extract timestamps and calculate time between errors
  - Identify the most frequent error types
  - Generate a summary report as a CSV file
- Branch: `task/advanced-analytics`

---
