# Pending Engram mirror — sdd-init/tesis-boilerplate

Created 2026-11-21. The parent session is bound to project `boilerfree`; writes targeting project `tesis-boilerplate` were refused with "could not confirm Engram session registration". `engram_mem_doctor --project tesis-boilerplate` reports 10/10 OK, so this is a session-scope limitation, not store damage.

Restore these three observations with `mem_save(capture_prompt: false, project: "tesis-boilerplate")` from a session bound to that project, then delete this file.

## 1. sdd-init/tesis-boilerplate

- type: `architecture`
- scope: `project`
- topic_key: `sdd-init/tesis-boilerplate`

**What**: Initialized SDD context for `tesis-boilerplate`, a thesis-writing vault rather than an application codebase.
**Why**: The immediate target is analyzing `Desarrollo_de_tesis.docx` and `SOLUCION.md`; treating the repo as a web app would invent a stack that is not present.
**Where**: Repo root `Tesis boilerplate/tesis-boilerplate`; `openspec/config.yaml`, `openspec/specs/.gitkeep`, `openspec/changes/archive/.gitkeep`, refreshed `.atl/skill-registry.md`.
**Learned**: Zero project markers, no workspace test runner or CI, Strict TDD false. APA 7 governs format (verify against `apuntes/Guia-Normas-APA-7ma-edicion.md`); the bibliography is authoritative for citation identity; `verificar_referencias.py --etiquetas` is explicit opt-in. `.docx` deliverables are binary duplicates of prose and must not be implicitly regenerated.

## 2. sdd/tesis-boilerplate/testing-capabilities

- type: `config`
- scope: `project`
- topic_key: `sdd/tesis-boilerplate/testing-capabilities`

**What**: Detected testing capabilities for `tesis-boilerplate` on 2026-11-21.
**Why**: Downstream SDD phases need to know whether automated tests exist before claiming verification.
**Where**: Project `.` — Markdown/Obsidian + Python 3 stdlib + `.docx`.
**Learned**: Strict TDD disabled; test command `—`, framework `—`; no unit, integration, E2E, coverage, lint, type-check or formatter. Only validation is `python verificar_referencias.py` (exit 0/1/2); `--fix` mutates files and `--etiquetas` is opt-in. Do not claim test execution in apply/verify.

## 3. skill-registry

- type: `config`
- scope: `project`
- topic_key: `skill-registry`

**What**: Refreshed skill registry for `tesis-boilerplate` on 2026-11-21.
**Why**: Delegators need exact `SKILL.md` paths rather than generated summaries.
**Where**: `.atl/skill-registry.md`; user-level paths under `C:\Users\luisP\.config\opencode\skills`.
**Learned**: Seven non-SDD skills registered: `chained-pr`, `cognitive-doc-design`, `go-testing`, `judgment-day`, `skill-creator`, `skill-improver`, `work-unit-commits`. No project-local convention scan matches. Pass only matching paths to subagents.
