# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([9b019375 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:9b019375b3b96aee8cca4e16803dc9a5bd1a2de8299ef3ef81ed159efca096f5")).
<!--[[[end]]] (checksum: 4bb8e23f30fd1d5d04398d20ddb28c36)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                                          | Version                                                         | License                 | Author            | Description (from packaging data)                                  |
|:------------------------------------------------------------------------------|:----------------------------------------------------------------|:------------------------|:------------------|:-------------------------------------------------------------------|
| [aiohttp](https://github.com/aio-libs/aiohttp)                                | [3.8.1](https://pypi.org/project/aiohttp/3.8.1/)                | Apache Software License | UNKNOWN           | Async http client/server framework (asyncio)                       |
| [asyncpg](https://github.com/MagicStack/asyncpg)                              | [0.26.0](https://pypi.org/project/asyncpg/0.26.0/)              | Apache Software License | MagicStack Inc    | An asyncio PostgreSQL driver                                       |
| [atlassian-python-api](https://github.com/atlassian-api/atlassian-python-api) | [3.27.0](https://pypi.org/project/atlassian-python-api/3.27.0/) | Apache Software License | Matt Harasymczuk  | Python Atlassian REST API Wrapper                                  |
| [attrs](https://www.attrs.org/)                                               | [22.1.0](https://pypi.org/project/attrs/22.1.0/)                | MIT License             | Hynek Schlawack   | Classes Without Boilerplate                                        |
| [starlette](https://github.com/encode/starlette)                              | [0.20.4](https://pypi.org/project/starlette/0.20.4/)            | BSD License             | Tom Christie      | The little ASGI library that shines.                               |
| [typer](https://github.com/tiangolo/typer)                                    | [0.6.1](https://pypi.org/project/typer/0.6.1/)                  | MIT License             | Sebastián Ramírez | Typer, build great CLIs. Easy to code. Based on Python type hints. |
| [uplink](https://uplink.readthedocs.io/)                                      | [0.9.7](https://pypi.org/project/uplink/0.9.7/)                 | MIT License             | P. Raj Kumar      | A Declarative HTTP Client for Python.                              |
| [websockets](https://github.com/aaugustin/websockets)                         | [10.3](https://pypi.org/project/websockets/10.3/)               | BSD License             | Aymeric Augustin  | An implementation of the WebSocket Protocol (RFC 6455 & 7692)      |
<!--[[[end]]] (checksum: daba4ad369c4d8c2bfd4d3dbf84a7419)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
aiohttp==3.8.1
  - aiosignal [required: >=1.1.2, installed: 1.2.0]
    - frozenlist [required: >=1.1.0, installed: 1.3.0]
  - async-timeout [required: >=4.0.0a3,<5.0, installed: 4.0.2]
  - attrs [required: >=17.3.0, installed: 22.1.0]
  - charset-normalizer [required: >=2.0,<3.0, installed: 2.1.0]
  - frozenlist [required: >=1.1.1, installed: 1.3.0]
  - multidict [required: >=4.5,<7.0, installed: 6.0.2]
  - yarl [required: >=1.0,<2.0, installed: 1.7.2]
    - idna [required: >=2.0, installed: 3.3]
    - multidict [required: >=4.0, installed: 6.0.2]
asyncpg==0.26.0
atlassian-python-api==3.27.0
  - deprecated [required: Any, installed: 1.2.13]
    - wrapt [required: >=1.10,<2, installed: 1.14.1]
  - oauthlib [required: Any, installed: 3.2.0]
  - requests [required: Any, installed: 2.28.1]
    - certifi [required: >=2017.4.17, installed: 2022.6.15]
    - charset-normalizer [required: >=2,<3, installed: 2.1.0]
    - idna [required: >=2.5,<4, installed: 3.3]
    - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.10]
  - requests-oauthlib [required: Any, installed: 1.3.1]
    - oauthlib [required: >=3.0.0, installed: 3.2.0]
    - requests [required: >=2.0.0, installed: 2.28.1]
      - certifi [required: >=2017.4.17, installed: 2022.6.15]
      - charset-normalizer [required: >=2,<3, installed: 2.1.0]
      - idna [required: >=2.5,<4, installed: 3.3]
      - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.10]
  - six [required: Any, installed: 1.16.0]
starlette==0.20.4
  - anyio [required: >=3.4.0,<5, installed: 3.6.1]
    - idna [required: >=2.8, installed: 3.3]
    - sniffio [required: >=1.1, installed: 1.2.0]
typer==0.6.1
  - click [required: >=7.1.1,<9.0.0, installed: 8.1.3]
uplink==0.9.7
  - requests [required: >=2.18.0, installed: 2.28.1]
    - certifi [required: >=2017.4.17, installed: 2022.6.15]
    - charset-normalizer [required: >=2,<3, installed: 2.1.0]
    - idna [required: >=2.5,<4, installed: 3.3]
    - urllib3 [required: >=1.21.1,<1.27, installed: 1.26.10]
  - six [required: >=1.13.0, installed: 1.16.0]
  - uritemplate [required: >=3.0.0, installed: 4.1.1]
websockets==10.3
````
<!--[[[end]]] (checksum: 163d835b14c30b72dcc6f8f7d53079d0)-->
