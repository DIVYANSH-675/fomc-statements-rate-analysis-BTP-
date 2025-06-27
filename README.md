# FOMC Statements and Fed Funds Rate Analysis

> **B.Tech Project (5th Semester)**
> Under the guidance of **Mr. Santosh Kumar Mishra**

---

## Overview

This project analyzes **Federal Open Market Committee (FOMC)** statements alongside **Federal Funds Interest Rate** data to identify if changes in text language can be linked to rate changes.

The goal is to build a pipeline that:

* Scrapes FOMC statements.
* Cleans and preprocesses text data.
* Analyzes linguistic patterns.
* Attempts predictive modeling for rate changes.

---

## Project Files

### `FOMC_Web-Scrapping.ipynb`

Scrapes FOMC statements from the official website.

### `FOMC_Cleaning.ipynb`

Handles the cleaning and structuring of FOMC statement text.

* Uses a script adapted from Miguel Acosta ([www.acostamiguel.com](http://www.acostamiguel.com)), updated for Python 3.
* Cleans raw FOMC statements to remove headers, footers, and voting info.

### `FOMC.ipynb`

Main analysis notebook with tokenization, word frequency analysis, and optional modeling.

### `textmining_withnumbers.py`

Creates a **term-document matrix** to show how often each word appears in each document.

* Includes a tokenizer and a matrix generator.
* Useful for understanding word distributions across FOMC statements.
* Run this script to generate matrix-based insights.

---

## Setup Instructions (Run Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fomc-funds-analysis.git
cd fomc-funds-analysis
```

### 2. Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
# OR
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebooks

Use Jupyter Notebook or Jupyter Lab to run the `.ipynb` files:

```bash
jupyter notebook
```

Open each notebook in sequence:

* `FOMC_Web-Scrapping.ipynb`
* `FOMC_Cleaning.ipynb`
* `FOMC.ipynb`

### 5. Data Folder Structure

Ensure this structure:

```
statements/
├── statements.raw             # Raw input
├── statements.clean           # Cleaned output
└── statements.clean.np       # Normalized (not used)
```

---

## Resource Used

**Research Paper Reference:**
["Trillion Dollar Words: A New Financial Dataset, Task & Market Analysis"](https://arxiv.org/abs/2305.13441)
Authors: Agam Shah, Suvan Paturi, Sudheer Chava

---

## Project By

**Divyansh Gupta**
Department of Computer Science & Engineering
Rajiv Gandhi Institute of Petroleum Technology

