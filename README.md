# biocypher-components-registry
This is a simple repository to test a possible process to register BioCypher components

## How to register a component?

1. Clone this repository:
```bash
git clone https://github.com/ecarrenolozano/biocypher-components-registry.git
```
2. Open the file `adapters.yaml` and add the following:
```yaml
adapters:
  - name: <adapter_name_in_snake_case>
    metadata_url: <raw GitHub URL pointing to the Croissant JSON-LD metadata file in your adapter's repository>
```
`name`: Use the adapter’s name in snake_case format (e.g., my_adapter).

`metadata_url`: Provide the direct raw URL to the Croissant metadata file (croissant.jsonld) hosted in your adapter’s GitHub repository. This URL should point to the raw file content (e.g., https://raw.githubusercontent.com/username/repo/branch/croissant.jsonld).

3. That is all!