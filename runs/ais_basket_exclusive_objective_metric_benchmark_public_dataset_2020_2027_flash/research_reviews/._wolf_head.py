import io, re
fn = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all\00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md"
txt = io.open(fn, encoding="utf-8").read()
# find all lines that look like headings containing intro
for i, line in enumerate(txt.split("\n")):
    if "ntroduction" in line or "NTRODUCTION" in line:
        print(i, repr(line[:120]))