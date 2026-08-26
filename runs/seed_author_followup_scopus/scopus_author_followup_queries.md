# Scopus Queries for the Later Publications of the 20 Seed Papers' Authors

## Validation and definitions

- Seed records matched to complete Scopus metadata by EID: 20/20.
- Unique authors across all 20 seeds: 36.
- Unique first authors: 15.
- Core authors: 20.
- `core author` means either first author on at least one seed or an author appearing on at least two seed papers.
- Each follow-up clause uses `PUBYEAR AFT <latest seed year>` and therefore retrieves strict later calendar years after that author's last seed contribution.
- Scopus author profiles can be split or merged incorrectly. After retrieval, inspect the author profiles of important cases for alternate Author IDs.

## Core author map

| Author | Scopus Author ID | Role in seeds | Seed count | Last seed year | Seed IDs |
|---|---:|---|---:|---:|---|
| Bhadauria, Vikram S. | 55079190600 | first author | 1 | 2020 | 1 |
| Mahapatra, Radha Kanta | 56247833500 | recurring coauthor | 2 | 2020 | 1;5 |
| Nerur, Sridhar P. | 55897149500 | recurring coauthor | 2 | 2020 | 1;5 |
| Vijayasarathy, Leo | 6602663544 | first author | 1 | 2016 | 2 |
| Allen, Gove N. | 8750608700 | first author | 2 | 2010 | 3;9 |
| Balijepally, VenuGopal | 14017577500 | first author | 1 | 2009 | 5 |
| Bowen, Paul L. | 7102327208 | first author | 3 | 2009 | 4;8;11 |
| Rohde, Fiona H. | 7004397830 | recurring coauthor | 2 | 2009 | 4;8 |
| Goswami, Supama | 52363500600 | first author | 1 | 2008 | 6 |
| Chua, Cecil Eng Huang | 7103191337 | first author | 1 | 2006 | 7 |
| March, Salvatore T. | 7005489136 | recurring coauthor | 2 | 2006 | 9;18 |
| Shaft, Teresa M. | 6603262441 | first author | 3 | 2006 | 10;15;19 |
| Vessey, Iris | 7004429096 | recurring coauthor | 3 | 2006 | 10;15;19 |
| Borthick, A.Faye | 6508047569 | first author | 1 | 2001 | 11 |
| Janvrin, Diane | 23979685600 | first author | 1 | 2000 | 12 |
| Panko, Raymond R. | 7004273004 | first author | 2 | 1999 | 13;14 |
| Kim, Jinwoo | 33067745400 | first author | 1 | 1997 | 16 |
| Lee, Sunro | 24755947600 | first author | 1 | 1996 | 17 |
| Leitheiser, Robert L. | 6602595432 | first author | 1 | 1996 | 18 |
| Palvia, Prashant | 7004085979 | first author | 1 | 1991 | 20 |

## Recommended execution order

1. Run Query E0 to retrieve strict post-seed publications by all 36 authors. This is the primary exhaustive author-follow-up search.
2. If Scopus rejects the combined query because of interface/query-length constraints, run E1–E3 and merge the exports by EID.
3. Retain author role fields from `seed_author_map.csv` so first authors, recurring core coauthors, and other coauthors can be compared rather than pooled blindly.
4. Run Query D1 and D2 as topical views, not as replacements for the exhaustive E query.
5. Query A/B/C remain useful sensitivity analyses for complete careers, first-author continuity, and core-author continuity.

## Query A: all publications by the 15 unique first authors

This intentionally has no date or subject filter. It is the most robust export for reconstructing complete author trajectories locally.

```text
AU-ID(55079190600) OR AU-ID(6602663544) OR AU-ID(8750608700) OR AU-ID(14017577500) OR AU-ID(7102327208) OR AU-ID(52363500600) OR AU-ID(7103191337) OR AU-ID(6603262441) OR AU-ID(6508047569) OR AU-ID(23979685600) OR AU-ID(7004273004) OR AU-ID(33067745400) OR AU-ID(24755947600) OR AU-ID(6602595432) OR AU-ID(7004085979)
```

## Query B: strict post-seed publications by first authors

```text
(AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991)
```

## Query C: strict post-seed publications by 20 core authors

```text
(AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(56247833500) AND PUBYEAR AFT 2020)
OR (AU-ID(55897149500) AND PUBYEAR AFT 2020)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(7004397830) AND PUBYEAR AFT 2009)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(7005489136) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(7004429096) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991)
```

## Query D1: core-author follow-up restricted to programming-related topics

```text
((AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(56247833500) AND PUBYEAR AFT 2020)
OR (AU-ID(55897149500) AND PUBYEAR AFT 2020)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(7004397830) AND PUBYEAR AFT 2009)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(7005489136) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(7004429096) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991))
AND
TITLE-ABS-KEY(
  "computer program*" OR programmer* OR programming OR coding OR
  "software develop*" OR "software engineer*" OR "software maintenan*" OR
  "program comprehension" OR "software comprehension" OR "code comprehension" OR
  "source code" OR debugging OR "software testing" OR "code review" OR
  "code inspection" OR "pair programming" OR "test-driven development" OR
  "end-user computing" OR "end-user development" OR "end-user programming" OR
  spreadsheet* OR "query formulation" OR "query development" OR
  "SQL quer*" OR "database quer*" OR "code generation"
)
```

## Query D2: core-author follow-up restricted to modern GenAI-assisted programming

```text
((AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(56247833500) AND PUBYEAR AFT 2020)
OR (AU-ID(55897149500) AND PUBYEAR AFT 2020)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(7004397830) AND PUBYEAR AFT 2009)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(7005489136) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(7004429096) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991))
AND
TITLE-ABS-KEY(
  ("generative AI" OR "generative artificial intelligence" OR
   "large language model*" OR LLM OR ChatGPT OR Copilot OR Codex OR
   "AI assistant*" OR "AI-assisted" OR "artificial intelligence-assisted" OR
   "coding agent*" OR "programming agent*" OR "software engineering agent*")
  AND
  (programming OR coding OR programmer* OR developer* OR "software engineering" OR
   "software development" OR "source code" OR "code generation" OR debugging OR
   testing OR "code review" OR "program comprehension")
)
```

## Query E: strict post-seed publications by every seed author

### Query E0: all 36 authors in one combined query

```text
(AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(56247833500) AND PUBYEAR AFT 2020)
OR (AU-ID(55897149500) AND PUBYEAR AFT 2020)
OR (AU-ID(7102658138) AND PUBYEAR AFT 2016)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(55220552900) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(55939037700) AND PUBYEAR AFT 2009)
OR (AU-ID(7201789505) AND PUBYEAR AFT 2009)
OR (AU-ID(7004397830) AND PUBYEAR AFT 2009)
OR (AU-ID(55663541300) AND PUBYEAR AFT 2008)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7410131022) AND PUBYEAR AFT 2008)
OR (AU-ID(14831184400) AND PUBYEAR AFT 2006)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(6506131540) AND PUBYEAR AFT 2006)
OR (AU-ID(7005489136) AND PUBYEAR AFT 2006)
OR (AU-ID(6603892218) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(7003462863) AND PUBYEAR AFT 2006)
OR (AU-ID(7004429096) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(15734744700) AND PUBYEAR AFT 2001)
OR (AU-ID(57198726776) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7403196226) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(7102105763) AND PUBYEAR AFT 1998)
OR (AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(36902722400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7103070629) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991)
```

Use E1–E3 below only as a fallback if the Scopus interface rejects E0 or if smaller exports are easier to manage.

### Query E1: all-author follow-up chunk 1

```text
(AU-ID(55079190600) AND PUBYEAR AFT 2020)
OR (AU-ID(56247833500) AND PUBYEAR AFT 2020)
OR (AU-ID(55897149500) AND PUBYEAR AFT 2020)
OR (AU-ID(7102658138) AND PUBYEAR AFT 2016)
OR (AU-ID(6602663544) AND PUBYEAR AFT 2016)
OR (AU-ID(8750608700) AND PUBYEAR AFT 2010)
OR (AU-ID(55220552900) AND PUBYEAR AFT 2010)
OR (AU-ID(14017577500) AND PUBYEAR AFT 2009)
OR (AU-ID(7102327208) AND PUBYEAR AFT 2009)
OR (AU-ID(55939037700) AND PUBYEAR AFT 2009)
OR (AU-ID(7201789505) AND PUBYEAR AFT 2009)
OR (AU-ID(7004397830) AND PUBYEAR AFT 2009)
OR (AU-ID(55663541300) AND PUBYEAR AFT 2008)
OR (AU-ID(52363500600) AND PUBYEAR AFT 2008)
OR (AU-ID(7410131022) AND PUBYEAR AFT 2008)
```
### Query E2: all-author follow-up chunk 2

```text
(AU-ID(14831184400) AND PUBYEAR AFT 2006)
OR (AU-ID(7103191337) AND PUBYEAR AFT 2006)
OR (AU-ID(6506131540) AND PUBYEAR AFT 2006)
OR (AU-ID(7005489136) AND PUBYEAR AFT 2006)
OR (AU-ID(6603892218) AND PUBYEAR AFT 2006)
OR (AU-ID(6603262441) AND PUBYEAR AFT 2006)
OR (AU-ID(7003462863) AND PUBYEAR AFT 2006)
OR (AU-ID(7004429096) AND PUBYEAR AFT 2006)
OR (AU-ID(6508047569) AND PUBYEAR AFT 2001)
OR (AU-ID(15734744700) AND PUBYEAR AFT 2001)
OR (AU-ID(57198726776) AND PUBYEAR AFT 2001)
OR (AU-ID(23979685600) AND PUBYEAR AFT 2000)
OR (AU-ID(7403196226) AND PUBYEAR AFT 2000)
OR (AU-ID(7004273004) AND PUBYEAR AFT 1999)
OR (AU-ID(7102105763) AND PUBYEAR AFT 1998)
```
### Query E3: all-author follow-up chunk 3

```text
(AU-ID(33067745400) AND PUBYEAR AFT 1997)
OR (AU-ID(36902722400) AND PUBYEAR AFT 1997)
OR (AU-ID(24755947600) AND PUBYEAR AFT 1996)
OR (AU-ID(6602595432) AND PUBYEAR AFT 1996)
OR (AU-ID(7103070629) AND PUBYEAR AFT 1996)
OR (AU-ID(7004085979) AND PUBYEAR AFT 1991)
```

## Export recommendation

Export CSV with at least: authors, full author names, Author IDs, title, year, source title, cited-by count, DOI, EID, abstract, author keywords, and index keywords. If Scopus offers a `References` export option, include it; otherwise the export can reconstruct topics and careers but not the complete cited-reference matrix.
