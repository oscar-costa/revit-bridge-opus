# Revit OPUS Bridge

A pyRevit-based tool to import OPUS cost estimation files (`.opux`, `.mdb`) into Revit workflows by converting them into a normalized JSON format.

---

## 🚀 Overview

**Revit OPUS Bridge** provides a structured and scalable way to:

- Read OPUS budget files (`.opux`, `.mdb`)
- Extract cost data (groups and concepts)
- Normalize the data into a consistent JSON schema
- Track versions and source integrity using a `manifest.json`

This enables integration between **cost estimation workflows (OPUS)** and **BIM environments (Revit)**.

---

## 🧠 Key Concepts

### 🔹 ETL Pipeline

The tool follows a simple ETL approach:

```
OPUS (.opux / .mdb)
        ↓
Extract
        ↓
Normalize
        ↓
JSON output
        ↓
Used in Revit / pyRevit
```

---

### 🔹 Manifest System

Each project maintains a `manifest.json` file that tracks:

- Active budget JSON
- Source OPUS file
- File integrity (hash)
- Version history

#### Example:

```json
{
  "active": "presupuesto_2026-03-31_1530.json",
  "source": {
    "type": ".opux",
    "path": "\\\\server\\costs\\projectX\\budget.opux",
    "hash": "a94f8c3b2d1e4f6a7b8c9d0e12345678"
  },
  "history": [
    "presupuesto_2026-03-31_1015.json",
    "presupuesto_2026-03-31_1530.json"
  ]
}
```

---

## 📁 Project Structure

```
revit-opus-bridge/
│
├── extension/              # pyRevit extension
├── lib/                    # core logic (extract, transform, utils)
├── schemas/                # JSON schemas
├── examples/               # sample files
├── tests/                  # unit tests
├── docs/                   # documentation
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/revit-opus-bridge.git
```

---

### 2. Add extension to pyRevit

Link the `extension/` folder:

```
pyrevit extensions add <path-to-extension>
```

---

### 3. Reload pyRevit

```
pyrevit reload
```

---

## ▶️ Usage

1. Open Revit
2. Go to the **Revit OPUS Bridge** tab
3. Click **Import OPUS**
4. Select a `.opux` or `.mdb` file
5. The system will:
   - Extract data
   - Generate a JSON file
   - Update `manifest.json`

---

## 📦 Output

### JSON Budget File

Contains:

- Groups (hierarchy)
- Concepts
- Key properties:
  - code
  - description
  - unit
  - unit price

---

### Manifest File

Located at:

```
/data/opus/manifest.json
```

Acts as the **single source of truth** for:

- Active dataset
- Source file reference
- Version tracking

---

## 🔐 Design Decisions

- JSON as the primary data format
- No local copy of OPUS files (external reference only)
- Hash-based change detection
- Flat + relational data model (not deeply nested)
- Schema stability (no breaking changes in manifest keys)

---

## ⚠️ Requirements & Notes

- OPUS `.mdb` support requires:
  - Microsoft Access ODBC Driver (64-bit)

- Use UNC paths for network files:

  ```
  \\server\folder\file.opux
  ```

- Avoid mapped drives (e.g. `Z:\`)

---

## 🧪 Testing

Run tests with:

```
pytest
```

---

## 🛣️ Roadmap

- [ ] XML parser refinement for `.opux`
- [ ] MDB schema auto-detection
- [ ] JSON schema validation
- [ ] pyRevit UI improvements
- [ ] Revit parameter integration
- [ ] Budget comparison (diff between versions)

---

## 🤝 Contributing

Contributions are welcome. Please:

- Follow code structure
- Keep naming conventions consistent
- Do not modify existing JSON schema keys

---

## 📄 License

MIT License

---

## 💡 Vision

This project aims to become a **bridge between cost estimation and BIM**, enabling:

- Data-driven construction workflows
- Cost validation inside Revit
- Integration with analytics and automation pipelines

---
