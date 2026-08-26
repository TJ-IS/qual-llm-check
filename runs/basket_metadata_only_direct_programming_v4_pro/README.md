# Basket metadata-only direct-programming audit

This audit screens the 31 records that:

1. occur in the complete 17,745-record Basket metadata CSV;
2. match the existing high-recall programming query; and
3. have no corresponding decision in the earlier 13,910-full-text screen.

Each bibliographic record is sent in one independent request to `deepseek-v4-pro`. The prompt applies the strict programming-specific replacement test using title, abstract, and keywords only. An initial V4 Flash attempt was terminated before producing output after the endpoint stalled; no Flash decisions are mixed into this run.
