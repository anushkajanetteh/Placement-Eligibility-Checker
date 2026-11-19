import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from main import offline_extract, is_valid, check_facts, job_status, is_eligible

students = [
 {"roll":"1","name":"A","branch":"CSE","cgpa":8.0,"backlogs":0,"batch":2027},
 {"roll":"2","name":"B","branch":"IT","cgpa":7.0,"backlogs":0,"batch":2027},
 {"roll":"3","name":"C","branch":"MECH","cgpa":7.2,"backlogs":1,"batch":2027},
 {"roll":"4","name":"D","branch":"ECE","cgpa":8.5,"backlogs":0,"batch":2026},
 {"roll":"5","name":"E","branch":"EEE","cgpa":6.8,"backlogs":0,"batch":2027},
]
cases = [
 ("CSE students of 2027 batch. Minimum CGPA 7.5. No backlogs.","matched",1),
 ("Any branch can apply. Minimum CGPA 6.5.","matched",5),
 ("Mechanical and EEE students of 2027 batch. Minimum 70 percent.","needs_review",0),
 ("ECE students. Minimum CGPA 8.0.","matched",1),
 ("Students of 2027 batch. Minimum CGPA 7.0.","needs_review",0),
]
failures=0
print("EVALUATION HARNESS")
for i,(post,want_status,want_count) in enumerate(cases,1):
 c=offline_extract(post)
 ok=is_valid(c) and check_facts(post,c)
 status=job_status(c) if ok else "needs_review"
 count=sum(is_eligible(s,c) for s in students) if status=="matched" else 0
 passed=status==want_status and count==want_count
 print(f"Test {i}: expected ({want_status}, {want_count}), got ({status}, {count}) - {'PASS' if passed else 'FAIL'}")
 failures += not passed
print(f"{len(cases)-failures}/{len(cases)} passed")
if failures: raise SystemExit(1)
