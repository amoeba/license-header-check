# license-header-check

Checks file headers for the given software license template.

Numerous other solutions can be found online but many make certain choices about how license text should appear in headers.
This package tries to be as flexible as possible.

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
TODO
```

## Contributing

TODO
