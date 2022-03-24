# policies

Policy documents for services run by New Vector Ltd (trading as Element)

## Versioning

Documents are versioned using semver:

- Major bump - significant change requiring subjects' specific re-acknowledgement/acceptance
- Minor bump - notable change in text, but not something that would require subjects' specific attention
- Patch bump - fixing a typo

Versioning metadata is stored in the top of the policy doc - each doc has a metadata segment inspired by gatsby that looks something like:

```
---
title: Document Title
version 1.0.0
---
```

Identity servers and integration managers manage tracking subjects' 'accepted terms' by tracking the URL representing those terms - it is therefore *imperative* that any generated links to docs include the major version _and only the major version_ (e.g. https://example.com/document-title-1) so that only a change in the major version triggers the 're-optin' flow.

### Versioning Tooling

`/scripts/versions.py` will mine the github commit history for a given document and output a file representing the most recent state of that document for each numbered version. `versions.py` doesn't handle templating or markdown->html.

To apply this to all of the policy docs:

```
for FILE in $(find docs -name '*.md' | grep -v README.md); do ./scripts/versions.py $FILE; done;
```

## Templating

Most of these files are templated using `{{ variable_name }}`, to be digested by ansible/jinja2 somewhere down the line for deployment to different instances. To apply Element data to the templates, you can use [jinja2-cli](https://pypi.org/project/jinja2-cli/):

```
$ jinja2 <filename> ~/path/to/new_vector.json --format=json
```

## Turning the Markdown into HTML

This section needs some work. You can generate a full set of html docs from the .md source using:

```
npm run build
```

This will create a `/build` directory with a folder structure mirroring `/docs`, with a .html file in place of every .md file.

At the moment this does not play nicely with `versions.py`, and it is questionable whether it is a good idea at all to have a build system as part of the docs repo when, in some instances at least (such as the matrix.org website) what's needed is a markdown file that gatsby will then ingest.
