import pandas as pd

df = pd.read_csv("data/bible_data_set.csv")

def search_and(keywords):
    """Return verses that contain ALL keywords."""
    results = df.copy()
    for kw in keywords:
        results = results[results["text"].str.lower().str.contains(kw)]
    return results

def search_or(keywords):
    """Return verses that contain ANY of the keywords."""
    pattern = "|".join(keywords)  # regex OR
    return df[df["text"].str.lower().str.contains(pattern)]

def main():
    print("Simple Bible Search (supports multiple keywords)")
    print("Examples: 'love truth', 'god world'")
    print("Use AND by default, or type 'or: love truth' for OR search")

    while True:
        query = input("\nSearch (or 'exit'): ").strip().lower()
        if query == "exit":
            break
        if not query:
            continue

        # Detect OR mode: user types "or: love world"
        if query.startswith("or:"):
            keywords = query.replace("or:", "").strip().split()
            results = search_or(keywords)
        else:
            # Default: AND mode
            keywords = query.split()
            results = search_and(keywords)

        if results.empty:
            print("No matches found.")
        else:
            for _, row in results.iterrows():
                ref = f"{row['book']} {row['chapter']}:{row['verse']}"
                print(f"- {ref} — {row['text']}")