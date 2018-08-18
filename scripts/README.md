# Data.World - Validate Data

## Prerequisites
* a Curator created GitHub branch 
* a data processing script
* GitHub account
* Data.World personal free account
* Data.World personal authorization token
* Citizen Labs membership
* Jupyter Notebook installed 
* Local install of "[Adopt a Drain]"(https://github.com/citizenlabsgr/adopt-a-drain)

## Setup Repo
* First time Setup 
```
### First 
# clone to local
git clone https://github.com/citizenlabsgr/data.world.git
cd data.world
# setup Environment variables
### Refresh Repo
cd data.world
git pull
```
## Setup Environment Variables
* Open command window in repo folder data.world
```
cd data.world/scripts/adopt-a-drain
GH_USER=your-github-user-name >> .env
DW_USER=your-data-world-user-name >> .env
DW_AUTH_TOKEN=dataworld-adm-token >> .env
```
## Validate Raw Data
* Open command window in repo folder data.world
```
# start jupyter notebook
cd scripts/adopt-a-drain
jupyter-notebook
```

## Validate Raw Data
* Test Load Data 
    * open comand window
    * cd data.world/
## Test "Adopt a Drain" Application
## Notifiy Maintainer
* push branch 



