# Publish package with poetry

## Configure forgejo repository

    # https://gitea.example.com/api/packages/{owner}/pypi
    
    poetry config repositories.forge-dev http://172.16.8.9:3000/api/packages/heubuchm/pypi

    poetry config http-basic.forge-dev heubuchm


## Publish package

    poetry publish -r forge-dev