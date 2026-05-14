# Contributing

Thanks for helping improve Awesome Defence.

This repository is meant to be a curated, useful map of public physical-defence-adjacent resources. Please keep submissions high-signal, relevant, and based on sources that are openly available.

## Inclusion Criteria

A resource should:

- Fit the scope of physical defence, defence equipment, emergency response, unmanned systems, sensing, C2, geospatial tools, field communications, simulation, logistics, or related research.
- Be useful to practitioners, researchers, maintainers, or serious learners.
- Have a clear README, documentation, paper, dataset card, standard, or hardware description.
- Prefer open-source software, source-available repositories, open hardware, public papers, public datasets, public standards, or official documentation.
- Be placed in the most specific relevant section.

## Quality Criteria

Avoid submitting:

- Spam, SEO pages, affiliate links, or link farms.
- Broken links or projects with no usable public material.
- Repos, papers, or datasets with unclear provenance.
- Context-only news articles, landscape pieces, commentary, and status updates.
- Duplicates unless the new entry adds meaningful context.
- Abandoned forks with no unique value unless historically important.
- Standalone courses or tutorials unless the repository also provides reusable code, data, standards, or hardware assets.
- Non-defence resources with no clear connection to the scope.

## Entry Format

Use this format:

```md
- [Name](URL) - One-sentence description. `OSS` `Active`
```

Good:

```md
- [QGroundControl](https://github.com/mavlink/qgroundcontrol) - Cross-platform ground control station for MAVLink-compatible drones. `OSS` `Active`
```

Avoid:

```md
- QGC - drone stuff
```

## Tags

Use tags sparingly:

- `OSS` - Open-source software with a visible open-source license
- `Source-available` - Public source repository without a verified open-source license
- `HW` - Open hardware or hardware design files
- `Dataset` - Dataset, benchmark, or corpus
- `Paper` - Public paper, preprint, or academic publication
- `Standard` - Protocol, standard, or interoperability artifact
- `Index` - Curated list, directory, or source hub
- `Active` - Recently maintained or visibly active
- `Archive` - Inactive but historically useful
- `Dual-use` - Has both civilian and military/defence applications
- `Fork` - Fork retained because it has curated value distinct from, or newer than, the upstream repository

The machine-readable tag vocabulary is kept in `data/tags.json`.

## Duplicate Entries

Before adding a duplicate URL, check `docs/duplicate-urls.md` and make sure the repeated entry adds useful section-specific context.

## Validation

Run the local validator before submitting a pull request:

```sh
python3 scripts/validate_readme.py --check-duplicate-report docs/duplicate-urls.md
```

If your change intentionally adds or removes a cross-section duplicate, regenerate the duplicate report:

```sh
python3 scripts/validate_readme.py --write-duplicate-report docs/duplicate-urls.md
```

## Pull Request Checklist

- [ ] The resource fits the repository scope.
- [ ] The link is public and working.
- [ ] The description is neutral, concise, and useful.
- [ ] The entry is in the most relevant section.
- [ ] The entry uses the standard format.
- [ ] Metadata tags use the vocabulary in `data/tags.json`.
- [ ] Any duplicate URL is intentional and reflected in `docs/duplicate-urls.md`.
- [ ] `python3 scripts/validate_readme.py --check-duplicate-report docs/duplicate-urls.md` passes.
- [ ] The source and provenance are clear enough for a curated list.

## Maintenance Notes

Maintainers may remove entries that disappear, are taken over by spam, lose public access, have unclear provenance, or no longer fit the scope.
