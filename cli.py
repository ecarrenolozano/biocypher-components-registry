import json
import os
import argparse

REGISTRY_DATA_DIR = "registry_data"
AGGREGATED_FILE = "unified_adapters_metadata.jsonld"


def list_adapters():
    if not os.path.isfile(AGGREGATED_FILE):
        print(
            f"Aggregated metadata file '{AGGREGATED_FILE}' not found. Please generate it first."
        )
        return

    with open(AGGREGATED_FILE, "r") as f:
        data = json.load(f)
        adapters = data.get("@graph", [])

    if not adapters:
        print("No adapters found in the aggregated metadata.")
        return

    print("Registered adapters:")
    for adapter in adapters:
        name = adapter.get("name", "Unknown")
        version = adapter.get("version", "Unknown")
        print(f"- {name} (version: {version})")


def inspect_adapter(name):
    if not os.path.isfile(AGGREGATED_FILE):
        print(
            f"Aggregated metadata file '{AGGREGATED_FILE}' not found. Please generate it first."
        )
        return

    with open(AGGREGATED_FILE, "r") as f:
        data = json.load(f)
        adapters = data.get("@graph", [])

    for adapter in adapters:
        if adapter.get("name") == name:
            print(json.dumps(adapter, indent=2))
            return

    print(f"Adapter '{name}' not found in the registry.")


def export_metadata(output_file):
    if not os.path.isfile(AGGREGATED_FILE):
        print(
            f"Aggregated metadata file '{AGGREGATED_FILE}' not found. Please generate it first."
        )
        return

    with open(AGGREGATED_FILE, "r") as f:
        data = json.load(f)

    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Exported aggregated metadata to '{output_file}'")


def main():
    parser = argparse.ArgumentParser(description="BioCypher Adapters Registry CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all registered adapters")

    inspect_parser = subparsers.add_parser(
        "inspect", help="Inspect metadata of a specific adapter"
    )
    inspect_parser.add_argument("name", help="Name of the adapter to inspect")

    export_parser = subparsers.add_parser(
        "export", help="Export aggregated metadata to a file"
    )
    export_parser.add_argument("output_file", help="File path to export metadata")

    args = parser.parse_args()

    if args.command == "list":
        list_adapters()
    elif args.command == "inspect":
        inspect_adapter(args.name)
    elif args.command == "export":
        export_metadata(args.output_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
