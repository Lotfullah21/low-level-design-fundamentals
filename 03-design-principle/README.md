### DRY, KISS, YAGNI

General guidelines for writing better code.

- `Category`: General software engineering principles
- `Focus`: Overall code quality and development approach
- `Scope`: Any programming paradigm (OOP, functional, procedural, etc.)
- `Origin`: Industry best practices, emerged organically over time

#### DRY, KISS, YAGNI answer:

- Should I write this code at all? (YAGNI)
- Am I repeating myself? (DRY)
- Is this too complicated? (KISS)

##### Visual Hierarchy

```sh
Software Design Principles
│
├── General Principles (any paradigm)
│   ├── DRY (Don't Repeat Yourself)
│   ├── KISS (Keep It Simple, Stupid)
│   └── YAGNI (You Aren't Gonna Need It)
│
└── OOP-Specific Principles
    └── SOLID
        ├── Single Responsibility
        ├── Open/Closed
        ├── Liskov Substitution
        ├── Interface Segregation
        └── Dependency Inversion
```

### Summary Comparison

| Principle | Focus       | Mantra                                         |
| --------- | ----------- | ---------------------------------------------- |
| DRY       | Maintenance | "Don't duplicate logic. One source of truth."  |
| KISS      | Readability | "Don't be clever. Be clear."                   |
| YAGNI     | Efficiency  | "Don't build it until the client asks for it." |

### Quick Comparison Table

| Aspect       | SOLID                    | DRY, KISS, YAGNI     |
| ------------ | ------------------------ | -------------------- |
| Type         | OOP Design Rules         | General Guidelines   |
| When Created | 2000s (formalized)       | Evolved over decades |
| Formality    | Strict acronym (5 rules) | Loose principles     |
| Language     | OOP languages            | Any language         |
| Level        | Architecture/Design      | Code quality         |
| Example      | "Use interfaces"         | "Don't copy-paste"   |
