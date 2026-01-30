# Notes

- The agent behaves reliably when tasks emphasize extraction over action.
- Phrasing the task to explicitly request output improves stopping behavior.
- Many apparent failures were caused by missing observability, not bad
  decisions.
- Retry logic can mask root causes unless logs are read carefully.
- Headed mode is useful for understanding why an agent stopped or diverged.
