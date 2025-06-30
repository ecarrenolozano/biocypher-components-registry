import argparse
import json
import os

REGISTRY_FILE = os.path.join("registry_data", "unified_registry.jsonld")


def list_adapters():
    with open(REGISTRY_FILE, "r") as f:
        registry = json.load(f)
    for adapter in registry.get("adapters", []):
        print(f"{adapter.get('name')} - version {adapter.get('version')}")


def inspect_adapter(name):
    with open(REGISTRY_FILE, "r") as f:
        registry = json.load(f)
    for adapter in registry.get("adapters", []):
        if adapter.get("name") == name:
            print(json.dumps(adapter, indent=2))
            return
    print(f"Adapter {name} not found in registry.")


def export_registry():
    with open(REGISTRY_FILE, "r") as f:
        data = json.load(f)
    print(json.dumps(data, indent=2))


def main():
    parser = argparse.ArgumentParser(description="BioCypher Adapter Registry CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all adapters")

    inspect = subparsers.add_parser("inspect", help="Show metadata for adapter")
    inspect.add_argument("name", help="Adapter name")

    subparsers.add_parser("export", help="Export full registry in Croissant JSON-LD")

    args = parser.parse_args()

    if args.command == "list":
        list_adapters()
    elif args.command == "inspect":
        inspect_adapter(args.name)
    elif args.command == "export":
        export_registry()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
