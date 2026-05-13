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

## Duplicate Review

The duplicate report tracks URLs that appear in more than one section. Cross-section duplicates are allowed when the resource is genuinely useful in each category, but same-section duplicates should be removed.

After intentionally adding or removing a cross-section duplicate, regenerate the report:

```sh
python3 scripts/validate_readme.py --write-duplicate-report docs/duplicate-urls.md
```

## Metadata

Allowed tags are defined in `data/tags.json`. Keep README legend text, `CONTRIBUTING.md`, and `data/tags.json` aligned when changing the tag vocabulary.
