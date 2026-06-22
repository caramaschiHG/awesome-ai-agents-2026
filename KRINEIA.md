# KRINEIA.md — awesome-ai-agents-2026

**krineia_manifest_version:** 0.1
**schema:** krineia-manifest@0.1

This is the repo-local KRINEIA manifest for `hummbl-dev/awesome-ai-agents-2026`.

---
krineia_manifest_version: "0.1"
schema: "krineia-manifest@0.1"

repo:
  full_name: "hummbl-dev/awesome-ai-agents-2026"
  visibility: "public"
  status: "archived"

authority:
  steward: "HUMMBL Research Institute"
  approving_human: "Reuben Bowlby"

governance_profile:
  status: "archived_fork"
  krineia_required: false
  trust_root_mode: "deployment_asserted"
  fork_of: "caramaschiHG/awesome-ai-agents-2026"

chains:
  primary:
    chain_id: "awesome-ai-agents-2026-primary"
    storage: "_receipts/krineia/primary.jsonl"
    genesis_policy: "not_bootstrapped"
    hash_algorithm: "sha256"

operators:
  allowed:
    - "append"
    - "project"
    - "cut"

boundaries:
  no_reward_path_self_reference: true
  external_analysis_only: true
  observed_agent_may_write_receipts: false
  receipts_may_train_agents: false

last_reviewed: "2026-06-22"
---

## Notes

### Archived fork

This repository is an archived fork of `caramaschiHG/awesome-ai-agents-2026`. No KRINEIA chain is bootstrapped. If this fork is ever un-archived and brought into active development, it must:

1. Bootstrap a genesis receipt in `_receipts/krineia/primary.jsonl`.
2. Adopt the full HUMMBL Repo Standard v0.1 artifact stack.
3. Open an ADR documenting the transition.

### No active governance

Archived forks do not require receipts, ADRs, or handoff notes. The fork boundary is declared in `HUMMBL_FORK.md` and `hummbl.repo.yaml`.
