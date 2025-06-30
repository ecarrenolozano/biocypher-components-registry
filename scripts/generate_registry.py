import os
import json

REGISTRY_DATA_DIR = "registry_data"
OUTPUT_FILE = os.path.join(REGISTRY_DATA_DIR, "unified_registry.jsonld")


def load_adapter_metadata():
    adapters = []
    for adapter_name in os.listdir(REGISTRY_DATA_DIR):
        adapter_path = os.path.join(REGISTRY_DATA_DIR, adapter_name)
        if not os.path.isdir(adapter_path):
            continue
        metadata_file = os.path.join(adapter_path, "croissant.jsonld")
        if os.path.exists(metadata_file):
            with open(metadata_file, "r") as f:
                md = json.load(f)
                md["@id"] = (
                    f"{md.get('github_repo', '')}#{md.get('name', '')}-{md.get('version', '')}"
                )
                adapters.append(md)
    return adapters


def generate_registry():
    adapters = load_adapter_metadata()
    registry_doc = {
        "@context": "https://w3id.org/croissant/v1",
        "type": "BioCypherAdapterRegistry",
        "adapters": adapters,
    }
    with open(OUTPUT_FILE, "w") as f:
        json.dump(registry_doc, f, indent=2)
    print(f"Unified registry written to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_registry()
