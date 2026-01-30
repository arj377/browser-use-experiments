# browser-use-experiments
Small exploratory experiments to understand Browser Use agent behavior and failure modes.

# Browser Use – Agent Experiments

This repo contains a small set of experiments I ran while exploring the
Browser Use agent framework locally.

The goal was not to build a product, but to understand how a real browser
agent behaves end-to-end: how tasks are interpreted, where failures occur,
and what observability is available when things go wrong.

## What I tried

- Ran a Browser Use agent locally using Python and the default Browser Use
  Cloud model.
- Gave the agent goal-oriented tasks (GitHub navigation, product search)
  rather than step-by-step instructions.
- Observed behavior in both successful and failing runs.

## What broke (and why)

- Invalid or missing API keys cause silent-looking failures unless logs are
  inspected.
- Agents often stop early if the task does not explicitly ask for a return
  value.
- Multi-constraint tasks are sensitive to phrasing and UI ambiguity.
- Most failures were interface or observability failures, not reasoning
  failures.

## What I learned

- Constraining the action space matters more than prompt cleverness.
- Clear stopping conditions are critical for reliability.
- Agent history is the most valuable debugging surface.
- Browser agents are strongest at selection and extraction, weaker at
  commitment (logins, carts, irreversible actions).

This repo is intentionally small and exploratory.
