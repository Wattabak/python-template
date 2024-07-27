# python-template

A collection of best-practices for handling python projects,
with various recipes for building using different projects 


## Build

setuptools-git-versioning is used to enable the versions of the packages be handled through git tags

## Dependencies

It turns out now there is a way to install packages directly from pyproject.toml, 
so you dont actually need to provide a setup.py file. 
If you add a git dependency like in the example below, `poetry install` command is going to use pyproject.toml settings, 
not the ones in setup.py. 
[More on git dependencies in poetry](https://python-poetry.org/docs/master/dependency-specification/)

```toml
parser_gibdd = { git = "https://github.com/Wattabak/parser-gibdd.git", branch = "package_init" }
```


## Development

<hr/>

## Local environment

Setting up postgis for local development

```shell
docker run -e POSTGIS_PASSWORD=mypassword -e POSTGIS_USER=myuser -p 5432:5432 --name postgis -d grenzeit
```

Setting up neo4j for local development

```shell
 docker run \          
    --name neo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v $HOME/neo4j/data:/data \
    -v $HOME/neo4j/logs:/logs \
    -v $HOME/neo4j/import:/var/lib/neo4j/import \
    -v $HOME/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/test \
    neo4j:latest
```

### Running tests

```shell
# assuming the local dev environment is set up
 pytest tests -vvv
```

