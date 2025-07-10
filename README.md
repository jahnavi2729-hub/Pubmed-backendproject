#  PubMed Paper Finder with LLM-Based Non-Academic Author Filtering

This is a command-line tool that allows you to search scientific articles on PubMed and automatically extract papers with at least one **non-academic (pharmaceutical or biotech)** author. The classification is performed using an LLM (Mistral-7B via OpenRouter), making it a smart and realistic solution for real-world biomedical data filtering.



---

##  Objective

-  Use an LLM to distinguish between **academic** and **non-academic** affiliations
-  Extract only papers with **non-academic pharma/biotech contributors**
-  Print results to terminal or save to CSV
-  Support clean, user-friendly CLI interface
-  Use typed, modular Python with proper error handling

---

##  Tech Stack

| Tool                | Purpose                                  |
|---------------------|-------------------------------------------|
| Python 3.11         | Programming language                      |
| OpenRouter API      | Hosts the LLM model (Mistral-7B-Instruct) |
| NCBI Entrez E-utilities | For querying PubMed articles            |
| Poetry              | Dependency and environment management     |
| dotenv              | Secure environment variable handling      |
| argparse            | CLI interface with flags and help         |

---

##  Project Structure

```
paper_finder/
├── __init__.py
├── pubmed.py              # Fetches and parses PubMed articles
├── filters.py             # LLM logic for filtering non-academic authors
├── utils.py               # CSV saving and terminal display
cli.py                     # CLI entry script
.env                       # Contains OpenRouter API Key (not shared)
pyproject.toml             # Poetry config
README.md                  # This file
```
##  Python Libraries Used

| Library        | Purpose                                      |
|----------------|----------------------------------------------|
| `requests`     | Sending API requests to OpenRouter           |
| `dotenv`       | To load `.env` and manage API keys securely  |
| `argparse`     | Build command-line interface (CLI)           |
| `csv`          | Save structured data to `.csv` format        |
| `typing`       | Type hints for better code quality           |
| `os`           | Environment variable and path handling       |
| `logging`      | Debug and info logs during development       |
---

##  LLM Integration Details
```
>Mistral 7B Instruct` hosted on OpenRouter

---

##  Environment Setup

### Step 1: Clone and enter project

git clone https://github.com/jahnavi2729-hub/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
```

### Step 2: Create `.env` file
Create a file named `.env` with your OpenRouter API key:
```
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxx
```

### Step 3: Install dependencies

poetry install
```

---

##  How to Use the CLI Tool

###  Basic interactive mode:

poetry run get-papers-list
```

It will ask:
```
 Enter a PubMed search query:
```

---

###  With direct query:

poetry run get-papers-list "gene therapy"
```

---

###  Save to CSV:

poetry run get-papers-list "checkpoint inhibitors" -f checkpoint.csv
```

---

###  With debug output:

poetry run get-papers-list "covid vaccine" --debug
```

---
## Sample Terminal Output

When filtered results are found:

```
---
PubmedID: 40633934
Title: Gene-expression signature predicts autoimmune toxicity in metastatic melanoma.
Publication Date: 2025-Jul-08
Non-academic Author(s): Michael Bailey; Sarah Warren
Company Affiliation(s): NanoString Technologies Inc.
Corresponding Author Email: example@email.com
```

---

##  CSV Output

If `-f` is provided, results are saved to `.csv` like:

| PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|-------|------------------|--------------------------|-------------------------|-----------------------------|
| 40633934 | Gene-expression... | 2025-Jul-08 | Michael Bailey | NanoString Inc. | example@email.com |

---

##  Error Handling

- Invalid affiliation structure → skipped with try-except
- API timeout or bad response → handled and logged
- No non-academic authors found → user is informed gracefully

---

##  Evaluation Criteria (from Aganitha's PDF)

| Requirement                                  | Status |
|----------------------------------------------|--------|
| Use of LLM for filtering                     | YES    |
| Typed Python & modular structure             | YES    |
| Efficient use of API + fallback logic        | YES    |
| Readable CLI tool                            | YES    |
| Option to export to CSV                      | YES    |
| Error handling for missing fields            | YES    |
| Video demonstration                          | YES    |
| Published module structure via Poetry        | YES    |

---

##  Demo Video

The accompanying `.mp4` file shows:
- Running the CLI
- Searching various queries
- LLM classification happening silently
- `.csv` file being saved and verified

---

##  Author

**Name**: Katta Jahnavi  
 **Email**: kattajahnavi27@gmail.com  
 **GitHub**: [https://github.com/jahnavi2729-hub](https://github.com/jahnavi2729-hub)

---


