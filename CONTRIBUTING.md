# Contributing to Awesome AI Agents 2026

Thanks for your interest in contributing! This list aims to be a reliable, current directory of resources in the AI agents ecosystem.

## Guidelines

### What belongs here
- AI agents, frameworks, platforms, and tools from 2025-2026
- Tools that are publicly available (released, beta, or open-source)
- Resources that are actively maintained

### What doesn't belong
- Abandoned projects (no updates in 6+ months)
- Purely theoretical / research-only projects without usable code
- Duplicate entries or very minor forks

### Format
Match the column count and order of the table in the section you are editing. Many sections use this three-column format:

```markdown
| [Name](https://link.com) | Brief, factual description. | Pricing info |
```

Some sections use fewer columns; do not add columns that are not present in that section's header.

### Process
1. Fork the repo
2. Create a branch: `git checkout -b add-tool-name`
3. Add your entry in the appropriate section
4. Ensure links work and descriptions are accurate
5. Run `python3 -m unittest discover -s tests -v` and `python3 scripts/check_catalog.py` for README catalog changes
6. Submit a PR

### PR Requirements
- [ ] Entry is in alphabetical order within its section
- [ ] Link is valid and points to official source
- [ ] Description is concise and factual
- [ ] Pricing info is current
- [ ] Time-sensitive pricing, availability, statistics, and clinical or safety claims cite a primary source and include a checked date where relevant
- [ ] No promotional language

## Updating Existing Entries
If you notice outdated information (pricing changes, new features, project status), please submit a PR with corrections.

## Suggesting New Categories
Open an issue first to discuss new category proposals before submitting a PR.

## Code of Conduct
Be respectful and constructive. We're all here to build a useful resource for the community.
