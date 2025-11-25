Simple Python project that lets users search the Bible for verses containing one or more keywords.
Includes:

* A **command-line version**
* A **Tkinter GUI version**
* Support for **AND** and **OR** keyword searching
* A reusable search module that loads the Bible dataset

---

## Structure

```
bible-search-project/
│
├── data/
│   └── bible_data_set.csv
│
├── src/
│   └── build_index.py        # Search logic (AND/OR) + CLI search
│
├── main.py                   # Runs the command-line interface
├── app.py                    # Runs the graphical UI (Tkinter)
└── README.md
```

---

## Features

### Multiple Keyword Search

* **AND search:** finds verses containing **all** keywords
* **OR search:** finds verses containing **any** keyword

### Two Ways to Use the App

1. **Command-line interface (CLI)**
2. **Graphical interface (Tkinter GUI)**

### Clean Architecture

The search functions live in `build_index.py` so both the CLI and UI can reuse them.

---

## Requirements

Install dependencies:

```bash
pip install pandas
```

(Only pandas is required; Tkinter comes with Python.)

---

## How to Run

### **1. Run the Command-Line Version**

```
python main.py
```

Example usage:

```
Search: love truth
Search: or: god world
Search: exit
```

---

### **2. Run the GUI (Tkinter) Version**

```
python app.py
```

This opens a window where you can type keywords and view matching verses.

---

## How It Works

### Keyword Search

The code loads the Bible dataset using:

```python
df = pd.read_csv("data/bible_data_set.csv")
```

Then provides two search modes:

* **search_and(keywords)** → every keyword must appear
* **search_or(keywords)** → at least one keyword must appear

Both functions return a filtered DataFrame of verses.

---

## Example File: build_index.py

This file contains:

* Data loading
* Search functions
* Text-based menu interface
* Reusable logic for both CLI and GUI versions

---

## Customization Ideas

Extend the project by:

* Adding case-insensitive highlight of matched words
* Adding book/chapter filters
* Integrating Streamlit for a web UI
* Showing search history
* Exporting found verses to a text file
