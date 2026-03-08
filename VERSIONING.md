# Versioning Specification

## Version Format
Semantic versioning in format: `X.Y.Z`
- X: Major version (breaking changes)
- Y: Minor version (new features, backwards compatible)
- Z: Patch version (bug fixes)

## Version Source
Version is stored in `VERSION` file in project root.

## Version Bumping
On push to main branch, the VERSION file must be updated.
CI workflow validates that VERSION was bumped.

## CI Validation
The CI workflow checks:
1. VERSION file exists
2. VERSION file contains valid semver format
3. On push to main, VERSION was modified from previous commit
