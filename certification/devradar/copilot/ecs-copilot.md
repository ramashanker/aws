## Setup infra

### Setup copilot

    curl -Lo copilot https://github.com/aws/copilot-cli/releases/latest/download/copilot-linux
    chmod +x copilot
    sudo mv copilot /usr/local/bin/copilot
    copilot --help

### Clone sample code

    git clone https://github.com/aws-containers/exploring-foundations-of-aws-containers.git


## On your own AWS account follow the steps in ppt

## Install and running

    cd exploring-foundations-of-aws-containers/app
    npm install
    node index.js

    curl -d "this is a test" localhost:3000

## Containerization

### Create docker file

    FROM public.ecr.aws/docker/library/node:18 AS build
    WORKDIR /srv
    ADD package.json package-lock.json ./
    RUN npm install

    FROM public.ecr.aws/docker/library/node:18-slim
    RUN apt-get update && apt-get install -y \
        curl \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* && apt-get clean
    COPY --from=build /srv .
    ADD . .
    EXPOSE 3000
    CMD ["node", "index.js"]

    
### Create docker image

    cd app
    docker build -t app .

## Verify docker image

    docker images

## Run docker container and verify

    docker run -d -p 3000:3000 --name reverse app
    docker ps -a
    curl -d "this is a test" localhost:3000
    docker logs reverse

### current resource consumption of any running containers

    docker stats

### Stop and remove the container

    docker rm -f reverse
    docker ps

## Deploy with  copilot

### Init the copilot and follow the ppt instruction

    cd ~/environment/exploring-foundations-of-aws-containers
    copilot init
    Note: If name exist create with new one





    
