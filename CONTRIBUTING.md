# Contribution Guidelines

### Environment Setup
Get all project dependencies:
```bash
pyenv install -r requirement.txt | pipenv install -r requirement.txt
```

And finally, run the project:
```bash
flask run
```

The title of the pull request should start with a [conventional commit] type.

Examples of such types:
- `[FIX]` - patches a bug and is not a new feature.
- `[FEAT]` - introduces a new feature.
- `[DOCS]` - updates or adds documentation or examples.
- `[TEST]` - updates or adds tests.
- `[REFACTOR]` - refactors code but doesn't introduce any changes or additions to the public API.

