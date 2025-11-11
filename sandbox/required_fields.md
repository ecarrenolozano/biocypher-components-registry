
## Required fields for Croissant file

required keys:
- [x] input format (flat file, database, parquet, API)
- [x] how many ontologies
- [x] which ontologies
- [x] ontology ID
- [x] adapter type (primary, secondary, low-code, MCP-based)
- [x] data types (metabolomics, proteomics, gene expression, genetics, clinical, molecular interaction, metadata)
- [x] data sources (resource url)
- [x] adapter url (code repo)
- [x] data license
- [x] adapter license
- [x] description of the adapter
- [x] homepage (of the project/group)
- [x] developer / github user id and/or orcid
- [x] Institute (uni heidelberg, helmholtz munich, ..., maybe some id) [ror.org]
- [x] biotoolsid [optional]
- [x] publications (DOI)  [optional]
- [x] domain/field (which identifier?) [investigate]
- [x] Elixiernode,country  [optional]
- [x] adapter name 
- [x] some tags ??
- [x] adapter version
- [x] test command to test the adapter
- [x] date of last change? initial date?

| **Field**             | **Group**                | **Notes / Description**                                            |
| --------------------- | ------------------------ | ------------------------------------------------------------------ |
| `adapter_name`        | Adapter Metadata         | Canonical name of the adapter or integration module                |
| `adapter_type`        | Adapter Metadata         | Classification: `primary`, `secondary`, `low-code`, or `MCP-based` |
| `adapter_version`     | Adapter Metadata         | Semantic version or release identifier                             |
| `description`         | Adapter Metadata         | Short summary of the adapter’s function and scope                  |
| `tags`                | Adapter Metadata         | Keywords for discoverability (domain, technology, etc.)            |
| `input_format`        | Data Description         | Source data access type: flat file, database, parquet, or API      |
| `data_types`          | Data Description         | Domain types such as metabolomics, proteomics, etc.                |
| `data_sources`        | Data Description         | External resources providing data, usually with URLs               |
| `data license`        | Data Description         | License of the input dataset (if distinct from adapter license)    |
| `how many ontologies` | Data Description         | Number of ontologies used in mapping                               |
| `which ontologies`    | Data Description         | Names or URIs of the ontologies integrated                         |
| `ontology ID`         | Data Description         | Ontology identifiers (e.g., GO, MONDO, PSI-MI)                     |
| `adapter_url`         | Adapter Metadata         | Repository or location of the adapter code                         |
| `test_command`        | Technical Information    | Command or script used for automated validation                    |
| `adapter_license`     | Adapter Metadata         | License governing the adapter source code                          |
| `developer`           | Provenance & Attribution | Primary author or maintainer information (name, GitHub, ORCID)     |
| `institute`           | Provenance & Attribution | Affiliated institution or research organization                    |
| `homepage`            | Provenance & Attribution | Project, lab, or group homepage                                    |
| `biotoolsid`          | Provenance & Attribution | [Optional] Link to bio.tools registry entry                        |
| `elixiernode`         | Provenance & Attribution | [Optional] Node within the Elixir network                          |
| `country`             | Provenance & Attribution | [Optional] Country of the developer or institution                 |
| `publications`        | References & Links       | [Optional] List of related publications (DOIs)                     |
| `domain/field`        | References & Links       | Scientific or technical domain identifier                          |
| `resource url`        | References & Links       | General link to the source data or project                         |
| `date of last change` | Lifecycle                | Last modification date (ISO 8601)                                  |
| `initial date`        | Lifecycle                | Initial creation date (ISO 8601)                                   |


## Yaml view

```yaml
adapter:
  name: "example-adapter"
  type: "primary"  # primary | secondary | low-code | MCP-based
  version: "1.0.0"
  description: "Adapter integrating proteomics data from UniProt into a unified ontology model."
  tags:
    - proteomics
    - ontology
    - uniprot
  adapter_license: "MIT"
  adapter_url: "https://github.com/example-org/proteomics-adapter"

data:
  input_format: "parquet"  # flat file | database | parquet | API
  data_types:
    - proteomics
    - molecular interaction
  data_sources:
    - url: "https://www.uniprot.org"
      license: "CC-BY-4.0"
  ontologies:
    count: 2
    list:
      - name: "GO"
        ontology_id: "go"
      - name: "Chebi"
        ontology_id: "chebi"

technical:
  test_command: "pytest tests/"  

provenance:
  developer:
    name: "Edwin Carreño"
    github: "edwincarreno"
    orcid: "0000-0002-1234-5678"
  institute:
    name: "Helmholtz Munich"
    ror_id: "https://ror.org/01bj3aw27"
  homepage: "https://helmholtz-munich.de"
  biotools_id: "proteomics-adapter"
  elixir_node: "de"
  country: "Germany"

references:
  publications:
    - doi: "10.1038/s41587-020-0456-0"
  domain: "Bioinformatics"

lifecycle:
  created: "2024-05-12"
  last_updated: "2025-11-10"

```

## Croissant View
```json
{
  "@context": {
    "@language": "en",
    "@vocab": "https://schema.org/",
    "cr": "http://mlcommons.org/croissant/"
  },
  "@type": "Dataset",
  "name": "example-adapter",
  "description": "Adapter integrating proteomics data from UniProt into a unified ontology model.",
  "version": "1.0.0",
  "license": "MIT",
  "url": "https://github.com/example-org/proteomics-adapter",
  "keywords": ["proteomics", "ontology", "uniprot"],
  "additionalType": "cr:Adapter",
  "cr:adapterType": "primary",
  "distribution": [
    {
      "@type": "DataDownload",
      "name": "Adapter Repository",
      "contentUrl": "https://github.com/example-org/proteomics-adapter",
      "encodingFormat": "git+https"
    }
  ],
  "cr:data": {
    "@type": "cr:DataSpecification",
    "cr:inputFormat": "parquet",
    "cr:dataTypes": ["proteomics", "molecular interaction"],
    "cr:dataSources": [
      {
        "@type": "DataDownload",
        "contentUrl": "https://www.uniprot.org",
        "license": "CC-BY-4.0"
      }
    ],
    "cr:ontologies": [
      {
        "@type": "CreativeWork",
        "name": "GO",
        "identifier": "go"
      },
      {
        "@type": "CreativeWork",
        "name": "Chebi",
        "identifier": "chebi"
      }
    ]
  },
  "creator": {
    "@type": "Person",
    "name": "Edwin Carreño",
    "identifier": [
      { "@type": "PropertyValue", "propertyID": "GitHub", "value": "edwincarreno" },
      { "@type": "PropertyValue", "propertyID": "ORCID", "value": "0000-0002-1234-5678" }
    ],
    "affiliation": {
      "@type": "Organization",
      "name": "Helmholtz Munich",
      "identifier": {
        "@type": "PropertyValue",
        "propertyID": "ROR",
        "value": "https://ror.org/01bj3aw27"
      },
      "url": "https://helmholtz-munich.de",
      "location": {
        "@type": "Place",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "Germany"
        }
      }
    }
  },
  "citation": [
    {
      "@type": "CreativeWork",
      "identifier": "https://doi.org/10.1038/s41587-020-0456-0"
    }
  ],
  "about": {
    "@type": "Thing",
    "name": "Bioinformatics"
  },
  "temporalCoverage": "2024-05-12/2025-11-10",
  "cr:testCommand": "pytest tests/",
  "cr:biotoolsId": "proteomics-adapter",
  "cr:elixirNode": "de"
}
```