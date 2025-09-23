# license-header-check

Checks file headers for the given software license template.
Designed to be used with [pre-commit](https://pre-commit.com).

Numerous other solutions can be found online but many make certain choices about how license text should appear in headers.
This package tries to be as flexible as possible.
The original approach was by [lidavidm](https://github.com/lidavidm) and [amoeba](https://github.com/amoeba) converted it into a package for use with [pre-commit](https://pre-commit.com).

## Installation

```sh
pip install .
```

## Usage

```sh
license_header_check --template "Copyright \(c\) [YEAR] My Company, Inc\.  All rights reserved\." some_file.cc
```

## pre-commit

This package is designed to be used with [pre-commit](https://pre-commit.com).
Here's an example...

```yaml
repos:
  - repo: https://github.com/amoeba/license-header-check
    rev: v0.1
    hooks:
      - id: license-header-check
        args:
          - "--template"
          - >-
            Copyright \(c\) [YEAR] My Company Inc\.  All rights reserved\.

```

Note: Using teh `>-` may be critical for your use case because `|` in YAML adds a newline.

## Contributing

Please file [Issues](https://github.com/amoeba/license-header-check/issues) to report bugs, request features, or ask for help.
