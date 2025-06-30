import os
import shutil
import yaml

ADAPTERS_YAML = "adapters.yaml"
REGISTRY_DATA_DIR = "registry_data"


def main():
    with open(ADAPTERS_YAML, "r") as f:
        config = yaml.safe_load(f)
    adapters = config.get("adapters", [])

    os.makedirs(REGISTRY_DATA_DIR, exist_ok=True)

    for adapter in adapters:
        name = adapter["name"]
        repo = adapter["repo"]
        print(f"Processing adapter: {name}")

        # For prototype, just copy metadata from local repo path
        src_path = repo
        dst_path = os.path.join(REGISTRY_DATA_DIR, name)
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path)
        print(f"Copied adapter {name} metadata.")


if __name__ == "__main__":
    main()
