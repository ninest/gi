# gi

> Easily create a .gitignore

![PyPI](https://img.shields.io/pypi/v/gi-cli?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/gi-cli?style=flat-square)
![GitHub](https://img.shields.io/github/license/ninest/gi?style=flat-square)

## Usage

```bash
# Install it
$ pip install gi-cli

# Add a language framework
$ gi add python

# Or add multiple
$ git add node python

# Clear your gitignore
$ git clear

# Uninstall it
$ pip uninstall gi-cli
```

**Note**: Mac or Linux users may have to use `pip3` instead of `pip`.

## Build setup

Clone or fork the repository, then run the commands:

```bash
poetry shell
poetry install
```

Add the pre-commit hooks:

```bash
pre-commit install
```

### Editor settings

```json
{
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.insertSpaces": true,
    "editor.detectIndentation": false,
    "editor.tabSize": 4
  },
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.pylintEnabled": false,

  "python.pythonPath": "/Users/username-here/Library/Caches/pypoetry/virtualenvs/xxx-py3.7"
}
```

## License

MIT
