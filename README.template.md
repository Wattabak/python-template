# {Project Name}

[//]: # (No longer than a paragraph)
{Short description}

## Dependencies

[//]: # ()
- Python 3.{x}
- Django {x.x}
- PostgreSQL 6

## Build

setuptools-git-versioning is used to enable the versions of the packages be handled through git tags

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

