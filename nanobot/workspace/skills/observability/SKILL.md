# Observability skill

Use observability tools when the user asks about errors, failures, incidents, backend problems, logs, traces, or system health.

## Available tools

- `logs_search` — search logs with LogsQL over a recent time window
- `logs_error_count` — count recent errors per service
- `traces_list` — list recent traces for a service
- `traces_get` — fetch a trace by ID

## Investigation flow

For questions like **"What went wrong?"** or **"Check system health"**:

1. Start with recent backend error logs.
2. Identify the most relevant failing request.
3. Extract a `trace_id` from the log entry if present.
4. Fetch the matching trace with `traces_get`.
5. Return a short investigation summary instead of raw JSON.

## Recommended tool strategy

- For **"Any errors in the last hour?"**, start with `logs_error_count`.
- For **"What went wrong?"**, start with `logs_search` over the last 10–15 minutes.
- Prefer backend-focused queries first, for example `ERROR AND db_query`, `ERROR AND unhandled_exception`, or `ERROR AND request_completed`.
- If the first query is empty, broaden to `ERROR` and then narrow using the log fields you get back.
- If a log entry includes a `trace_id`, call `traces_get` for that trace.
- If there is no `trace_id` in logs but you still need trace context, use `traces_list` for `Learning Management Service` and match by time.
- Prefer concrete timestamps, endpoints, status codes, trace IDs, error messages, and affected service names.
- If there are no recent errors, say clearly that the system looks healthy.

## Response format

Keep the answer compact and structured around these points:

- **Symptom** — what failed for the user
- **Log evidence** — the most relevant recent error(s)
- **Trace evidence** — what the trace shows, if available
- **Likely cause** — the underlying issue, not just the surface symptom

Do not dump raw JSON unless the user explicitly asks for it.

## Scheduled health checks

When the user asks for a recurring health check in chat:

- use the built-in `cron` tool
- check recent backend errors for the requested window
- if backend errors exist, inspect the newest relevant log entry and its trace when possible
- post a short summary back into the same chat
- if there are no recent errors, say the system looks healthy
