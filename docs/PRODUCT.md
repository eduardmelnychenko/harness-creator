# Product Requirements

## Purpose

An agent harness is the software, configuration, and documentation around a large language model (LLM) that enables it to perform goal-directed tasks. This product helps a user create a tailored agent harness through a natural-language conversation and produces a set of files that define the harness.

## Intended users and outcome

The intended user is a person who wants to describe an agent's goals and constraints without having to design every harness file by hand. At the end of a successful session, the user has a coherent set of harness files, understands the important choices made, and can identify any remaining setup they must perform.

## Scope

The product gathers requirements and generates harness files. It does not promise that a generated harness will work with every LLM, runtime, tool, or deployment environment. Compatibility depends on the requirements and supported targets made available by the product.

## Functional requirements

### Conversation and requirements

* The product must accept requirements expressed in natural language.
* It must gather enough information to define the requested harness, including its purpose, tasks, operating context, constraints, and desired outputs.
* It must let the user select one or more task types: regular software development, a machine learning (ML) task, or a data science task. It must also offer an `Other/custom` option for work that does not fit these categories. The product must use the selection to guide follow-up questions and capture relevant requirements without overriding the user's specific needs.
* For `Other/custom`, the product must ask focused questions to understand the task and its requirements. If it cannot support the clarified task, it must explain the limitation and must not present incomplete output as a complete harness.
* The user must be able to choose Claude Code as the target agent or choose another agent supported by the product. If the target is unclear or unsupported, the product must ask for clarification or explain the limitation.
* It must ask focused follow-up questions when required information is missing, ambiguous, or contradictory. It must not silently treat a material assumption as a confirmed requirement.
* It must retain relevant answers during the current harness-creation session and use them consistently in generated files.
* Before generation, it must summarize the captured requirements and surface unresolved assumptions or choices that could materially affect the result.
* It must let the user correct or clarify that summary before files are finalized.
* It must communicate limitations, missing information, and failures in terms the user can understand, and identify what input or action is needed next.
* The user may pause, resume, or restart a session at any time. Pause and resume must preserve and restore the full session state, including confirmed requirements, selected task types and target agent, unresolved questions, and generated drafts. Restart must begin a new session with the prior requirements and choices carried over as editable starting points, but without carrying over generated drafts. Restart must not delete files already generated or other user files.

### LLM provider configuration

* When the product uses an LLM, it must access providers through a shared provider-neutral interface.
* The product must support direct adapters for Ollama, OpenAI, Azure OpenAI, Meta's hosted API, Google Gemini, and Anthropic Claude.
* The default provider must be Ollama at a local endpoint. The user must be able to configure the provider and model.
* The product must report an unavailable or incorrectly configured provider and must not silently switch to another provider.

### Harness generation

* The product must convert the confirmed requirements into a coherent set of files that define the harness.
* Generated files and guidance must reflect the selected task type or combination of types, as well as the confirmed requirements.
* Generated files must follow the selected target agent's supported conventions and formats. The product must not present a harness for an unsupported target as compatible.
* Depending on the requested harness and supported targets, generated files may include configuration, source code, and documentation. The product must not imply that every harness requires every file type.
* Files that describe the same behavior must not contain known contradictions. If a requirement cannot be represented or generated, the product must identify it rather than silently omit it.
* The product must identify the purpose of generated files and any required user setup, such as credentials, dependencies, or environment-specific values. It must not include real credentials in generated output.
* The product must provide the user with access to the generated files and a way to distinguish generated content from information or files supplied by the user.
* The product must not silently overwrite existing user content. Before replacing or deleting user content, it must explain the effect and get the user's approval.
* When generation is incomplete or fails, the product must report which outputs are incomplete and must not present the result as a complete harness.

### Language and terminology

* User-facing conversation and human-readable generated text must use ASD-STE100 controlled English where applicable.
* Programming languages, configuration formats, identifiers, and other machine-readable syntax must remain valid for their target format. ASD-STE100 requirements apply to accompanying human-readable text, not to syntax that cannot conform to the standard.
* The product must use technical terms consistently and explain terms that the intended user may not know.

## Non-functional requirements

### Security and privacy

* The product must protect user requirements, conversation content, and generated files from unauthorized access.
* It must not expose secrets in messages, logs, examples, or generated files. It must identify secret values the user needs to supply without asking the user to disclose them in generated content.
* The product must explain relevant data handling, including whether session content is stored, where it is sent, and when it is removed. It must not claim privacy or retention guarantees that the implementation does not provide.
* Any external service or model use must be made clear to the user before data is sent to it.

### Reliability and correctness

* The product must preserve confirmed requirements throughout a session and must not report success when required generation or validation steps have failed.
* The product must report actionable errors when it cannot continue, generate a requested file, or validate an output.
* Generated files must conform to their declared formats. Where automated validation is available, the product must use it and report its result.

### Maintainability and extensibility

* The product must separate requirement gathering, harness generation, and output validation sufficiently to allow each capability to evolve without requiring unrelated changes.
* Supported harness targets, file types, and capabilities must be extendable without changing the meaning of existing requirements or silently changing previously supported behavior.
* Architecture and supported capabilities must be documented sufficiently for contributors to understand how to extend them.

### Usability and accessibility

* The conversation must present one clear question or decision at a time when user input is needed.
* The user must be able to understand progress, review important decisions, and know how to resume or correct the work when supported by the application.
* Errors and limitations must include a clear next action when one is available.
* User-facing flows must be usable with the accessibility capabilities supported by the product's interface and target environment.

## Acceptance criteria

A harness-creation session meets the product requirements when:

* The user can describe a harness request in natural language.
* The user can select one or more of regular software development, an ML task, or a data science task, and the product uses those selections to guide requirements and generated outputs.
* The user can select `Other/custom`; the product clarifies the task requirements or explains why it cannot support the task before presenting generated output as complete.
* The user can select Claude Code or another supported agent as the target. If the target is unsupported or unclear, the product asks for clarification or explains the limitation.
* The product asks for material missing or unclear information instead of silently guessing.
* The user can review and correct the captured requirements before final generation.
* Pausing and resuming restores the full session state, including requirements, task types, target agent, unresolved questions, and generated drafts. Restart creates a fresh session with prior requirements and choices as editable starting points, no carried-over drafts, and no deletion of existing files.
* The generated files represent the confirmed requirements consistently and follow the selected target agent's supported conventions, or the product identifies any requirement it could not fulfill and does not present unsupported output as compatible.
* The user can access the outputs and understand their purpose and required setup.
* User requirements, conversation content, and generated files are protected from access by unauthorized users.
* Secret values are not exposed in messages, logs, examples, or generated files. The product identifies secrets the user must supply without requesting that the values be included in generated content.
* Before user data is sent to an external service or model, the product explains which service receives it and the applicable data storage, transmission, and removal practices.
* The product does not replace or delete existing user content without explaining the effect and obtaining the user's approval.
* Generated files conform to their declared formats. When automated validation is available, the product runs it and reports the result.
* Invalid, incomplete, or failed generation is reported as such, with actionable information where possible.
* User-facing conversation and applicable human-readable output follow the language requirements above.
