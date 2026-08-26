# -*- coding: utf-8 -*-
import csv
p = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"
with open(p, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    r = csv.reader(fh)
    header = next(r)
    print("COLS:", len(header))
    for i, h in enumerate(header):
        print(i, repr(h))
    row = next(r)
    print("FIRST ROW:")
    for i, v in enumerate(row):
        print(i, repr(v[:120]))
