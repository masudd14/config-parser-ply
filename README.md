# Python Config File Parser using PLY (Lex & Yacc)

This project is a Python-based parser for reading configuration files that contain
**sections** and **key–value pairs**, similar to INI files.  
It uses the **PLY** library (Python Lex-Yacc) to tokenize and parse configuration
data and convert it into a structured **Python dictionary**.

---

## 🚀 Features

- Supports INI-style sections like `[SectionName]`
- Reads key–value pairs: `key = value`
- Handles:
  - Comments (`# ...`)
  - Blank lines
  - Global/default section
- Implemented using:
  - **Lex** (tokenizer)
  - **Yacc** (parser)
- Returns the final parsed configuration as a clean Python dictionary
---

## ✅ How To Run
You can see the result by runnig the main.py 

---

## 📦 Requirements

Install dependencies:

```bash
pip install ply
