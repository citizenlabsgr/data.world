# Validate Data

## Prerequisites
* Citizen Labs membership
* Merge pull request from Developer
* a data processing script maintainer/Maintainer.Process.ipynb
* Data.World personal free account
* Data.World personal authorization token
* Data.World/citizenslabs manager privileges
* Jupyter Notebook installed
* Local install of "[Adopt a Drain]"(https://github.com/citizenlabsgr/adopt-a-drain)

## Pull Requests
* Two kinds of pull requests
  * *Curator-pull-request*, named after the Curator and opened by Curator
  * *Developer-pull-request*, named after the Curator and opened by Developer
* You should ignore pull requests from Curators  

## GitHub
Clean data is now in the clean-data/ folder of the Developer-pull-request.  
* Merge Developer-pull-request to master

## Setup Repo
At this point, the
```
### Clone the master  
git clone https://github.com/citizenlabsgr/data.world.git
cd data.world
git checkout master
# check that Curator branch was down loaded
git branch
```

## Setup Environment Variables
* Open command window in repo folder data.world
```
cd data.world/scripts/adopt-a-drain
GH_OWNER=your-github-user-name >> .env
DW_OWNER=your-data-world-user-name >> .env
DW_AUTH_TOKEN=dataworld-adm-token >> .env
```
## Validate Raw Data
* Open command window in repo folder data.world
```
# start jupyter notebook
cd scripts/adopt-a-drain/maintainer
jupyter-notebook
```

# Run scripts/maintainer/maintainer.process.ipynb
