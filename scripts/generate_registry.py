import os
import json

REGISTRY_DATA_DIR = "registry_data"
OUTPUT_FILE = "unified_adapters_metadata.jsonld"  # renamed here


def load_all_metadata():
    all_metadata = []
    for filename in os.listdir(REGISTRY_DATA_DIR):
        if filename.endswith(".jsonld"):
            filepath = os.path.join(REGISTRY_DATA_DIR, filename)
            with open(filepath, "r") as f:
                try:
                    data = json.load(f)
                    all_metadata.append(data)
                except json.JSONDecodeError as e:
                    print(f"Skipping {filename} due to JSON error: {e}")
    return all_metadata


def main():
    metadata_list = load_all_metadata()
    aggregated = {"@context": "https://w3id.org/croissant/v1", "@graph": metadata_list}
    with open(OUTPUT_FILE, "w") as f:
        json.dump(aggregated, f, indent=2)
    print(f"Aggregated registry saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
