# Project History

This log records known project work from 2026-10-07 onward. It is not a complete record of work before that date.

## 2026-10-07 - Agent guidance and product requirements

* Expanded `AGENT.md` with startup guidance, project boundaries, conventions, feature-list handling, and definition-of-done criteria.
* Expanded `docs/PRODUCT.md` with product scope, conversational requirements gathering, harness generation, language requirements, security and privacy, reliability, extensibility, usability, and acceptance criteria.
* Validation: documentation-only changes; no application tests were run.

## 2026-10-08 - Harness target and task choices

* Added a choice between Claude Code and other supported agent targets.
* Added task-type selection for software development, machine learning, and data science.
* Validation: documentation-only changes; no application tests were run.

## 2026-10-09 - Acceptance criteria and agent workflow

* Added acceptance checks for target-agent selection and compatible output, security and privacy, secret handling, external-service disclosure, overwrite approval, and format validation.
* Defined combined task categories and an `Other/custom` option with clarification for unsupported tasks.
* Defined pause/resume to preserve full session state and restart to carry requirements and choices into a fresh, editable session without drafts or deleting existing files.
* Clarified feature-list initialization behavior in `AGENT.md` and added a one-work-unit-per-run rule with a summary and recommended next step.
* Established this file as the chronological project history and required an entry after each work unit.
* Validation: `git diff --check -- AGENT.md progress.md` passed. No application tests were run because the changes were documentation-only.

## History maintenance

Append one dated entry after each completed work unit. Include its scope, affected files, validation outcomes, and any important decisions, blockers, or follow-up work. Do not record secrets or private data.