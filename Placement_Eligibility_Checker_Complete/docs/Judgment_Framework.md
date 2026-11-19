# Judgment Framework

| Component | Risk | Check / decision |
|---|---|---|
| CSV loading | Missing columns or malformed values | Validate headers and numeric fields; stop with an error |
| LLM extraction | Invented criteria or malformed JSON | Validate exact schema; retry once; fallback |
| Branches | Branch inferred from job title | Accept only named branches; ALL only for any/all wording |
| CGPA | Percentage converted to CGPA | Never convert; missing explicit CGPA means review |
| Matching | Text comparison or wrong rule | Convert CGPA to float; apply only stated backlog/batch rules |
| Reports | Incorrect list shared | Keep as draft; placement officer checks every list |

**False exclusion:** An eligible student is omitted and may miss an opportunity.
**False inclusion:** An ineligible student is sent to a company and damages trust.
Both are important. The mandatory human checkpoint is the placement officer's review of every list before sharing.
