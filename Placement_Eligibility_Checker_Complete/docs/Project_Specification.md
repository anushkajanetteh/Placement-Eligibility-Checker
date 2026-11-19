# Project Specification — Placement Eligibility Checker

**Objective:** A console-based Python tool reads company job posts, extracts stated eligibility criteria, validates them against the post, and prepares draft lists of eligible students.

**Inputs:** `jobs.csv` has at least 8 rows and `id,company,post`; `students.csv` has at least 20 fictional records and `roll,name,branch,cgpa,backlogs,batch`.

**Privacy:** The LLM receives only job-post text. Student data remains local in Python and is never sent to the LLM.

**JSON contract:** Exactly five fields: `branches`, `min_cgpa`, `max_backlogs`, `batch`, `summary`. Branches are only explicitly named values from CSE, IT, AIDS, ECE, EEE, MECH, CIVIL, or `["ALL"]` only for any/all branches. CGPA is explicit 0–10 or null; never convert percentage. No backlogs means 0. Unstated backlog/batch is null. Summary is at most 12 words.

**Validation:** Validate schema, types, ranges and facts against the original post. Retry an invalid/unavailable LLM response once, then use a labelled offline fallback. Missing branch or CGPA means `needs_review`; otherwise `matched`.

**Eligibility:** Branch matches or ALL; CGPA meets cutoff; backlog count is within stated limit; batch matches when stated.

**Outputs:** `outputs/job_summary.csv`, `outputs/eligible.csv`, `outputs/review.csv`, and `outputs/summary.txt`.

**Edge cases:** Percentage cutoff is not converted; vague top-percent criteria are not converted to CGPA; unnamed branches are not inferred; untrusted instructions in a post cannot add a student; ambiguous or incomplete posts go to human review.

**Human checkpoint:** Placement officer checks every list against the original post and student records before sharing.
