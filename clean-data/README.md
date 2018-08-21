# Data.World - Validate Data

## Prerequisites
* a Curator created GitHub branch 
* the "01.Dev.Process.ipynb" processing script
* GitHub account
* Data.World personal free account
* Data.World personal authorization token
* Citizen Labs membership
* Jupyter Notebook installed 
* Local install of "[Adopt a Drain]"(https://github.com/citizenlabsgr/adopt-a-drain)

## Setup 
* First time Setup 

```
# open command window
# set script variables
curator_branch_name=Wilfongjt-patch-1
repo_url=https://github.com/citizenlabsgr/data.world.git
app_name=adopt-a-drain

# download curator branch
# identifiy curator by pattern: <curator-name>-patch-<N>
git clone -b ${curator_branch_name} ${repo_url}
cd data.world
git branch

## Open Jupyter Notebook
#if branch <curator-name>-patch-1 exists
# navigate to 
cd scripts/${app_name}
jupyter-notebook

```
## Validate Raw Data
Wait for Jupyter to open
Double-Click:  01.Dev.Process.ipynb
Click: Cell - Run All

## Update Repo
```
# assuming current folder is scripts/<app-name>
git add ../../clean-data/ -A
git commit -m "Data load from ${curator_branch_name}"
git push origin ${curator_branch_name}

```

```
### First 
# clone to local
git clone https://github.com/citizenlabsgr/data.world.git
cd data.world
git branch
git checkout  
# if needed pull curator branch
git checkout -b Wilfongjt-patch-1
git pull origin Wilfongjt-patch-1
git branch
# should have 
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
