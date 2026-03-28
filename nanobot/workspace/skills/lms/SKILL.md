# LMS skill

Use the LMS MCP tools to answer questions about labs, learners, scores, completion, activity, and system status.

## Available tools

- `lms_health` — check whether the LMS backend is healthy and how many items are loaded
- `lms_labs` — list all labs available in the LMS
- `lms_learners` — list learners
- `lms_pass_rates` — get pass rates, average scores, and attempts for a specific lab
- `lms_timeline` — get submission timeline for a specific lab
- `lms_groups` — get group performance for a specific lab
- `lms_top_learners` — get top learners for a specific lab
- `lms_completion_rate` — get completion rate for a specific lab
- `lms_sync_pipeline` — trigger backend sync if the user explicitly asks to refresh LMS data

## Tool usage strategy

- For “what labs are available?”, use `lms_labs`
- For architecture or system overview questions, first use `lms_health`, then `lms_labs`, and summarize the LMS as a backend-backed system exposing lab and learner analytics through tools
- For score, pass rate, completion, timeline, groups, or top learner questions, determine which lab is needed and then call the corresponding lab-specific tool
- If the user asks for scores, pass rates, completion, timeline, groups, or top learners but does not specify a lab, ask a short clarification question or list available labs first
- Do not guess lab ids; use `lms_labs` if needed
- Do not invent data that was not returned by tools
- If a tool returns an error, explain it briefly and suggest the next useful step
- Keep responses concise and factual

## Formatting rules

- Format percentages clearly, for example `73.5%`
- Format counts as plain integers
- When comparing labs or groups, present the key numbers directly
- Prefer short bullet lists only when they improve readability
- If the answer is based on one lab, mention the lab id explicitly

## Capability explanation

If the user asks “what can you do?” explain that you can:
- list labs
- inspect learners
- show pass rates
- show completion rate
- show submission timeline
- compare groups
- list top learners
- check LMS health

Also explain that some questions require a lab id, and if it is missing you will ask for it.
