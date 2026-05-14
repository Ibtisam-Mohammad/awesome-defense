# Maintenance

This repository is maintained as a curated index. The README is still the human-facing source of truth, with supporting machine-readable metadata in `data/`.

## Validation

Run the local validator before opening or merging a pull request:

```sh
python3 scripts/validate_readme.py --check-duplicate-report docs/duplicate-urls.md
```

Run the slower external link check when doing a broader maintenance pass:

```sh
python3 scripts/validate_readme.py --check-external
```

Run the resource audit when reviewing curation quality:

```sh
python3 scripts/audit_resources.py --check-git
```

The resource audit writes `docs/resource-audit.md`, which is ignored by git and intended as a local review queue rather than a committed report.

Set `GITHUB_TOKEN` or `GH_TOKEN` and add `--github-api` when you need repository metadata such as archived status, last push date, license, stars, topics, and GitHub-native descriptions:

```sh
GITHUB_TOKEN=... python3 scripts/audit_resources.py --check-git --github-api
```

The API-backed audit also raises review prompts for unverified `OSS` licenses, stale untagged repositories, GitHub forks, low-reuse signals, and raw GitHub description suggestions that can ground README wording.

## Duplicate Review

The duplicate report tracks URLs that appear in more than one section. Cross-section duplicates are allowed when the resource is genuinely useful in each category, but same-section duplicates should be removed.

After intentionally adding or removing a cross-section duplicate, regenerate the report:

```sh
python3 scripts/validate_readme.py --write-duplicate-report docs/duplicate-urls.md
```

## Metadata

Allowed tags are defined in `data/tags.json`. Keep README legend text, `CONTRIBUTING.md`, and `data/tags.json` aligned when changing the tag vocabulary.
