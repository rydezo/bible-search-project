import tkinter as tk
from tkinter import ttk, scrolledtext
from src import build_index

def run_search():
    query = entry.get().strip().lower()
    output_box.delete("1.0", tk.END)

    if not query:
        output_box.insert(tk.END, "Please enter keywords.\n")
        return

    # detect OR mode
    if query.startswith("or:"):
        keywords = query.replace("or:", "").strip().split()
        results = build_index.search_or(keywords)
    else:
        keywords = query.split()
        results = build_index.search_and(keywords)

    if results.empty:
        output_box.insert(tk.END, "No matches found.\n")
        return

    # display results
    for _, row in results.iterrows():
        ref = f"{row['book']} {row['chapter']}:{row['verse']}"
        text = row["text"]
        output_box.insert(tk.END, f"{ref} — {text}\n\n")


# ---- UI SETUP ----
root = tk.Tk()
root.title("Simple Bible Search")

window_width = 650
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Title
title = ttk.Label(root, text="Bible Search Tool", font=("Arial", 18))
title.pack(pady=10)

# Search bar
entry = ttk.Entry(root, width=50)
entry.pack(pady=5)

# Search button
btn = ttk.Button(root, text="Search", command=run_search)
btn.pack(pady=5)

# Results box
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25)
output_box.pack(pady=10)

root.mainloop()