# Maintainer Guide

This guide exists to keep Awesome AI Agents 2026 useful as submissions grow.

## Maintainer principle

Protect signal over volume. A smaller list with credible, well-placed entries is more valuable than a huge list of promotional submissions.

## Fast review flow

Use this flow for each PR:

1. Check whether the project is directly related to AI agents or agent workflows.
2. Check whether the link is official and free from UTM/referral parameters.
3. Search the README and open PRs/issues for duplicates.
4. Confirm the section is correct.
5. Check that the description is concise, factual, and non-promotional.
6. Reject unrelated churn, invisible encoding changes, broad rewrites, or formatting drift.
7. Approve only if the PR can be merged without lowering the quality bar.

## Suggested labels

Create these labels in GitHub when possible:

- `needs-review` — waiting for maintainer triage.
- `approved` — accepted and ready to merge.
- `needs-changes` — useful, but requires edits.
- `wrong-section` — entry belongs somewhere else.
- `duplicate` — duplicate entry, issue, or PR.
- `promotional` — too much marketing language.
- `needs-source` — claims need official/credible sources.
- `broken-link` — official link does not work.
- `category-proposal` — proposal for a new README section.
- `maintenance` — repository cleanup or documentation work.
- `good-first-review` — easy review for maintainers/contributors.

## Common approval comments

For a clean addition:

```text
Looks good. Focused README addition, appropriate section, and concise factual wording.
```

For an update to an existing entry:

```text
Looks good. This is a focused correction and keeps the existing table style intact.
```

## Common change request comments

Wrong section:

```text
Thanks for the contribution. I am not approving this yet because the entry appears to be in the wrong section. Please move it to the most relevant existing category and keep the description concise.
```

Duplicate:

```text
Thanks for the submission. I am not approving this because the project appears to already be listed or has another open PR/issue. Please consolidate the submission in the existing thread.
```

Promotional wording:

```text
Thanks for the contribution. I am not approving this yet because the description uses promotional or unverifiable claims. Please rewrite it in neutral, factual language.
```

UTM/referral link:

```text
Thanks for the contribution. Please remove UTM, referral, or tracking parameters from the URL and use the official canonical link.
```

Unrelated file churn:

```text
Thanks for the contribution. Please keep the PR focused on the intended entry only. Avoid unrelated formatting, encoding, or README-wide changes.
```

Not agent-specific enough:

```text
Thanks for the suggestion. I am not sure this is specific enough to AI agents or agent workflows. Please clarify the agent-specific use case or explain why it belongs in this list.
```

## When to close instead of request changes

Close the issue or PR when:

- It is clearly spam.
- It is unrelated to AI agents.
- It is a duplicate and there is already an active issue or PR.
- The project is only a consulting/agency page without a clear product.
- The submitter repeatedly ignores the contribution guidelines.

## Merge style

Prefer squash merges for contribution PRs so the history stays readable.

Suggested squash commit format:

```text
add <tool-name> to <section-name>
```

Examples:

```text
add AgentLine to voice agents
add Mneme HQ to governance and compliance
update contributing guidelines
```

## Monthly maintenance checklist

Once per month:

- Review open PRs and close stale duplicates.
- Check broken links in recently added entries.
- Remove or update abandoned projects if they no longer fit.
- Update the README top-line resource count if needed.
- Add a short release/changelog note for meaningful updates.

## Editorial stance

This repository should feel like a curated map, not a billboard. When in doubt, ask: would a builder researching AI agents genuinely thank us for including this?
