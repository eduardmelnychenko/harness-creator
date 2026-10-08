# Startup Rules
Before writing any code, complete these steps in order:

1. Read this file completely. It defines the boundaries and working rules for this project.
2. Read docs/ARCHITECTURE.md, if it contains content, to understand the app structure.
3. Read docs/PRODUCT.md to understand the product requirements.
4. Read feature_list.json, if it contains valid data, to understand the current feature status.
5. Inspect the repository for the relevant code, tests, and documented build or validation commands. Run `bash init.sh` only if that file exists.
6. If a required document is missing, empty, or invalid, do not invent its contents. Record the gap and continue only when it does not prevent the task. If a build or test fails, determine whether the failure is caused by the current change; fix task-related failures and report unrelated baseline failures without expanding the task.

## Boundaries

* Keep changes within the product requirements and the scope of the task. Do not add features or dependencies without a clear need.
* Preserve existing project behavior and conventions. Do not overwrite or discard unrelated user changes.
* Do not expose credentials, secrets, or private user data in source files, logs, examples, or generated output.
* Do not run destructive commands or make external changes unless the user explicitly requests them.
* Ask for clarification when requirements conflict or when a decision would materially change behavior. Otherwise, follow established project patterns and state any necessary assumptions.

## Conventions

* Follow the existing architecture, naming, formatting, and dependency patterns. When no pattern exists, use the standard conventions for the language and tools already in use.
* Reuse existing helpers and validation before adding new ones. Keep changes focused and add or update tests for changed behavior where tests are available.
* Keep documentation consistent with the implemented behavior and product requirements.
* Use ASD-STE100 for user-facing conversation and generated files where required by docs/PRODUCT.md. Do not silently claim compliance when it cannot be verified.

## Definition of Done
A feature is done when all applicable conditions are met:

* The implementation meets the agreed requirements and does not introduce known regressions.
* Relevant tests and available build or validation commands pass. If a check cannot run, record why.
* The app launches and operates without errors in the relevant normal-use flow, when the app is runnable.
* Generated or changed files meet their format and language requirements, where applicable.
* The feature is recorded in feature_list.json with status `pass` and evidence that supports the result.
* Documentation is updated when the change affects documented behavior.

## Working with the Feature List
The feature_list.json file is the source of truth for project feature status. Keep its existing structure and use these status values:

* `not-started`: work has not started.
* `pass`: all applicable done conditions are met; include verifiable evidence.
* `fail`: the feature does not meet its requirements; include the reason and remaining work.
* `blocked`: work cannot proceed; include the blocker and what is needed to continue.
* Do not mark a feature `pass` based only on implementation or an unverified assumption.
* Never delete features from the list. If the file is empty or invalid, do not invent feature statuses; report the issue and preserve the existing data.