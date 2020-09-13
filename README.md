# .gi

> **Easily add templates to your .gitignore**

## 🤔 Usage

- `gi` or `gi help`
- `gi add <templates>`
- `gi clear`

**Example**: Add the Python and Node .gitignore templates:

```bash
gi add python node
```

## ⚙️ Build setup

Clone or fork the repository, then run the commands:

```bash
pipenv shell
pipenv install
```

### Recommended editor settings

```json
{
  "python.formatting.provider": "black",
  "python.linting.flake8Enabled": true,
  "editor.formatOnSave": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "[python]": {
    "editor.insertSpaces": true,
    "editor.detectIndentation": false,
    "editor.tabSize": 4
  }
}
```
