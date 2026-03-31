# Revit OPUS Bridge

A pyRevit-based tool to import OPUS cost estimation files (`.opux`,
`.mdb`) into Revit workflows by converting them into a normalized JSON
format.

---

## 🚀 Overview

**Revit OPUS Bridge** provides a structured and scalable way to:

- Read OPUS budget files (`.opux`, `.mdb`)
- Extract cost data (groups and concepts)
- Normalize the data into a consistent JSON schema
- Track versions and source integrity using a `manifest.json`

---

## 🧠 Key Concepts

### 🔹 ETL Pipeline

OPUS (.opux / .mdb) → Extract → Normalize → JSON output → Used in Revit
/ pyRevit

---

### 🔹 Manifest System

Each project maintains a `manifest.json` file that tracks:

- Active budget JSON
- Source OPUS file
- File integrity (hash)
- Version history

---

## 📁 Project Structure

revit-opus-bridge/ ├── extension/ ├── lib/ ├── schemas/ ├── examples/
├── tests/ ├── docs/

---

## ⚙️ Installation

1.  Clone the repository: git clone
    https://github.com/your-username/revit-opus-bridge.git

2.  Add extension to pyRevit: pyrevit extensions add
    `<path-to-extension>`{=html}

3.  Reload pyRevit: pyrevit reload

---

## ▶️ Usage

1.  Open Revit
2.  Go to the Revit OPUS Bridge tab
3.  Click Import OPUS
4.  Select a .opux or .mdb file

---

## 📦 Output

### JSON Budget File

Contains: - Groups - Concepts - Properties: code, description, unit,
unit price

---

### Manifest File

/data/opus/manifest.json

---

## ⚠️ Notes

- `.mdb` requires Microsoft Access ODBC Driver (64-bit)
- Use UNC paths (\\server`\folder`{=tex}`\file`{=tex}.opux)
- Avoid mapped drives

---

## 🧪 Testing

pytest

---

## 📄 License

MIT License
