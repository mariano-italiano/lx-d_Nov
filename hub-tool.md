# Hub-tool

## Installation

```sh
wget https://github.com/docker/hub-tool/releases/download/v0.4.6/hub-tool-linux-amd64.tar.gz
tar -xvf hub-tool-linux-amd64.tar.gz
sudo install hub-tool/hub-tool /usr/bin/
```

## Usage

Before using, first login to Docker Hub:
```sh
hub-tool login
```

### Get all image tags

```sh
hub-tool tag ls nginx
hub-tool tag ls nginx --all
```
