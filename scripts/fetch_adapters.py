import os
import requests
import shutil
import yaml

ADAPTERS_YAML = "adapters.yaml"
REGISTRY_DATA_DIR = "registry_data"
METADATA_FILENAME = "croissant.jsonld"


def copy_local_metadata(name, local_path):
    src_path = os.path.join(local_path, METADATA_FILENAME)
    if not os.path.isfile(src_path):
        print(
            f"Metadata file {METADATA_FILENAME} not found locally for {name} at {src_path}"
        )
        return False

    os.makedirs(REGISTRY_DATA_DIR, exist_ok=True)
    dst_path = os.path.join(REGISTRY_DATA_DIR, f"{name}.jsonld")
    shutil.copyfile(src_path, dst_path)
    print(f"Copied local metadata for {name}")
    return True


def download_metadata(name, url):
    os.makedirs(REGISTRY_DATA_DIR, exist_ok=True)
    dst_path = os.path.join(REGISTRY_DATA_DIR, f"{name}.jsonld")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(dst_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded metadata for {name}")
            return True
        else:
            print(
                f"Failed to download metadata for {name}, HTTP status {response.status_code}"
            )
            return False
    except Exception as e:
        print(f"Exception during download for {name}: {e}")
        return False


def main():
    with open(ADAPTERS_YAML, "r") as f:
        config = yaml.safe_load(f)
    adapters = config.get("adapters", [])

    for adapter in adapters:
        name = adapter.get("name")
        local_path = adapter.get("local_path")
        metadata_url = adapter.get("metadata_url")

        print(f"Processing adapter: {name}")

        success = False
        if local_path:
            success = copy_local_metadata(name, local_path)
        if not success and metadata_url:
            success = download_metadata(name, metadata_url)

        if not success:
            print(f"WARNING: Failed to get metadata for adapter {name}")


if __name__ == "__main__":
    main()
