## Prerequisites

- [Python](https://www.python.org)
- [Pytest](https://docs.pytest.org/en/latest/)
- [VsCode](https://code.visualstudio.com)
- [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Usage

Tests are located only in `tests/` folder.

Empty functions, imported in tests, are located in `functions/` folder.

And finished functions are in `finished_functions/` folder.
To use them, simply change the imports in the `test_*.py` files from `functions.method_name` to `finished_functions.method_name`.
