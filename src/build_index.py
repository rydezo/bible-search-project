import pandas as pd

# load Bible CSV from same folder
df = pd.read_csv("data/bible_data_set.csv")

def search(keyword):
    keyword = keyword.lower()
    # Return all verses that contain the keyword (case-insensitive)
    matches = df[df["text"].str.lower().str.contains(keyword)]
    return matches

def main():
    print("Simple Bible Search")
    while True:
        query = input("\nEnter keyword (or 'exit'): ").strip()
        if query.lower() == "exit":
            break

        results = search(query)

        if results.empty:
            print("No results found.")
        else:
            for _, row in results.iterrows():
                ref = f"{row['book']} {row['chapter']}:{row['verse']}"
                print(f"- {ref} — {row['text']}")