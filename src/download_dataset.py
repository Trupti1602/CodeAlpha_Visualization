import urllib.request
from pathlib import Path

url = "https://raw.githubusercontent.com/leonism/sample-superstore/master/data/superstore.csv"


data_folder = Path(__file__).resolve().parent.parent / "data"
data_folder.mkdir(parents=True, exist_ok=True)


output_file = data_folder / "superstore.csv"

print("Downloading Superstore dataset...")

urllib.request.urlretrieve(url, output_file)

print(f"Dataset downloaded successfully!")
print(f"Saved to: {output_file}")

