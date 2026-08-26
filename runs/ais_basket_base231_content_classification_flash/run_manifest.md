# Run manifest

- Status: user approved on 2026-08-07.
- Input: the 231 locally saved full texts with `base_match=true` in the preceding screen.
- The previous theory-subset flag is joined after classification and is not included in the model prompt.
- Unit: one complete article per independent request.
- Model: `deepseek-v4-flash`.
- Maximum concurrency: 100.
- Prompts: copied from the user-confirmed Chinese draft; only headings changed to formal-run status.
- Output: `output_v1`; append-only decisions permit safe resume.
- No full text is copied or downloaded.
