## Important

# Python Module Naming Rules

**Rule:** A module name must start with a **letter or underscore**, and contain only **letters, digits, and underscores**.

| Status  | Module Name         |
| ------- | ------------------- |
| Valid   | `config.py`         |
| Invalid | `05-config.py`      |
| Invalid | `my-config.py`      |
| Invalid | `config manager.py` |
| Invalid | `2config.py`        |
| Valid   | `_config.py`        |
| Valid   | `app_config.py`     |
| Valid   | `config_manager.py` |

## Correction of Valid/Invalid Classification

Based strictly on Python’s module naming rules:

### These are actually **valid**:

```python
config.py
app_config.py
config_manager.py
_config.py

## Resources

[Singleton-patterns](https://refactoring.guru/design-patterns/singleton)
```

```py
from 05-config import app_config # invalid module name!
from config import app_config # valid module name!
```

## PEP 8 Module Naming Recommendations

PEP 8 recommends that module (file) names should be:

- **all lowercase**
- **use underscores when needed for readability**
- **avoid ambiguous abbreviations**
- **avoid using capital letters**

## Recommended Examples (PEP 8 compliant):

- `config.py`
- `app_config.py`
- `helpers.py`
- `database.py`
- `string_utils.py`
- `parser.py`
- `constants.py`
- `api_client.py`

---

## Avoid these (PEP 8 discouraged):

- `AppConfig.py` → PascalCase not recommended
- `myConfig.py` → contains uppercase
- `CONFIG.py` → ALL CAPS reserved for constants inside modules
- `string-utils.py` → hyphen is invalid
- `app config.py` → space is invalid
- `05config.py` → should not start with digits

---

## Additional Best Practices

- If a module name becomes very long with underscores, consider using a **package** instead.  
  Example: instead of:  
  `text_analysis_language_processing.py`  
  Better:

- Use leading underscore (`_module.py`) only when intentionally marking the module as **private/internal**.

- Try to choose names that describe the purpose clearly:
- `utils.py` → too vague
- `file_utils.py` → clearly about files
- `math_utils.py` → clearly about math
