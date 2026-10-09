# Architecture

## Status and scope

This document describes a proposed architecture for the product in `docs/PRODUCT.md`. The repository does not currently contain an application implementation, so the components and flows below are design boundaries, not claims about existing code or behavior. The baseline runtime, project tooling, persistence technology, and user interface are selected below. Frameworks, model providers, database schema and location, and deployment topology remain implementation choices.

The system turns a user's natural-language description into a reviewed, validated set of harness files for a supported task type and target agent. It does not guarantee compatibility with targets or environments that it does not support.

## Technology decisions

| Area | Decision |
| --- | --- |
| Runtime | Python 3.14 or later. |
| Project and dependency management | Use `uv` to manage the Python project, dependencies, virtual environment, and lockfile. Declare project metadata and dependencies in `pyproject.toml`; keep the generated `uv.lock` in sync with dependency changes. |
| Session persistence | Use SQLite. Access it through Python's standard-library `sqlite3` module unless a later requirement justifies another dependency. The schema, migration approach, database path, and retention policy are implementation details that must be documented when selected. |
| User interface | Use a line-oriented interactive terminal interface, not a full-screen TUI. Present a guided prompt-and-response flow that asks one clear question at a time and reports progress, errors, limitations, and generated file locations as readable terminal text. |

These choices define the product's baseline stack; they do not imply that the application or its persistence and terminal flows are implemented.

## Logical components

Keep these responsibilities separate so that conversation, generation, and validation can evolve independently:

| Component | Responsibility |
| --- | --- |
| Terminal interface | Implement the line-oriented prompt-and-response flow. Collect the user's request, present one focused question or decision at a time, show progress and limitations, and provide access to generated files. |
| Session coordinator | Direct the session through requirement gathering, review, generation, and completion. Request clarification when information is missing, ambiguous, or contradictory; do not convert material assumptions into confirmed requirements. |
| Requirements state | Hold the current request, task-type selections, target agent, confirmed answers, unresolved questions, and reviewable summary. Treat confirmed requirements as the shared source for all generated outputs and persist them in SQLite. |
| Task profiles | Supply focused questions and guidance for software development, ML, data science, and custom tasks. A custom task that cannot be supported must be identified before the result is presented as complete. |
| Target adapters | Describe a supported agent's conventions and capabilities. Check support before generation; do not label output compatible with an unsupported or unclear target. |
| Generation planner and renderers | Map confirmed requirements to the necessary output files, then create each file in the selected target's supported format. Include only file types required by the request and supported capabilities. |
| Output validator | Check generated files against their declared formats and available target-specific rules. Report validation results and errors; do not treat failed or incomplete generation as success. |
| Artifact manager | Present generated files and their purpose, distinguish them from user-supplied content, and identify setup the user must perform. Require approval before replacing or deleting user content. |
| Session persistence | Use SQLite to save and restore the complete session state needed to pause and resume, including requirements, selections, unresolved questions, and generated drafts. Its database location, retention, and deletion behavior must be explicit to the user. |

External models, tools, or services are dependencies at the boundary of the session coordinator or generation components. Before sending user data to one, explain which service receives it and the applicable storage, transmission, and removal practices. Do not assume a provider or make privacy guarantees that the implementation cannot support.

## Main flow

1. Start or restore a session in the terminal. A new session collects a natural-language request. A resumed session loads its full saved state from SQLite.
2. Gather requirements. Capture the user's purpose, tasks, operating context, constraints, desired outputs, selected task types, and target agent. Use task profiles to guide follow-up questions. Explain unsupported custom tasks or targets instead of silently substituting another capability.
3. Review requirements. Summarize the confirmed requirements and unresolved choices that could materially affect the result. Let the user correct the summary. Do not generate final files until material questions are resolved or clearly recorded as limitations.
4. Plan and generate. Select supported outputs from the confirmed requirements, target conventions, and available capabilities. Keep the files consistent with each other. Identify requirements that cannot be represented or generated.
5. Validate and present. Validate outputs where automated checks are available. Present the files, validation results, limitations, and required setup. Mark the result incomplete if a required output or check fails; do not describe it as a complete harness.
6. Pause, resume, or restart as requested. Pause and resume preserve the complete session state in SQLite, including drafts. Restart creates a new session with prior requirements and choices as editable starting points, but without prior generated drafts. Restart does not delete generated files or other user content.

## State and consistency

The session is the unit of work. Keep confirmed requirements, task and target selections, unresolved questions, generated drafts, and their status together in SQLite so they can be restored and reviewed. Persist related state changes together in database transactions so a failure does not leave a partially updated session. The schema and migration strategy are implementation decisions.

All generated files for a session must derive from the same confirmed requirements and selected target. When the user changes a confirmed requirement, update the shared session state and regenerate or revalidate affected outputs; do not leave known contradictions between files. Preserve the distinction between confirmed input, unresolved assumptions, generated content, and user-supplied content.

Do not store or emit secret values in generated files, messages, examples, or logs. Identify credentials and environment-specific values that the user must supply without asking them to place real values in generated content.

## Extension boundaries

- Add a task profile to define task-specific questions and guidance without changing the meaning of existing requirements.
- Add a target adapter to declare a target's supported conventions and capabilities. Gate generation and compatibility claims on that support.
- Add a renderer for a file type only when a supported target or requirement needs it. Keep output formats specific to their declared targets.
- Add validators alongside the formats and capabilities they check. A result is validated only to the extent that the available checks demonstrate.
- Keep orchestration independent from individual task profiles, target conventions, renderers, and validators. Extensions must not silently change previously supported behavior.

Document supported tasks, targets, file types, and validation limits as those capabilities become available. Do not infer support solely from an output that can be generated.

## Failure handling and safety

Surface actionable errors when requirements cannot be clarified, a target or task is unsupported, generation fails, or validation reports an issue. Identify affected outputs and the next action when one is available. Preserve recoverable session state and drafts when a session pauses or a step fails.

Before writing into a destination that contains user content, show what would change and get approval. Do not overwrite or delete content without that approval. Make the source and status of each presented artifact clear.

Limit access to the SQLite database, session content, and generated files to authorized users. Define and communicate the database path, retention, and removal behavior. Keep secrets out of logs and outputs. Explain data handling before external transmission, and ensure retention and removal descriptions match actual implementation behavior.

## Verification guidance

When implemented, verify the terminal prompt flow and its boundaries: requirement review and correction; supported and unsupported task/target handling; consistency across generated files; format validation and incomplete-generation reporting; SQLite pause/resume restoration; restart without carried-over drafts or deleted files; and approval before replacing user content. Test recovery from persistence failures, that secrets are not exposed, and that data-handling disclosures match configured external services and persistence behavior.
