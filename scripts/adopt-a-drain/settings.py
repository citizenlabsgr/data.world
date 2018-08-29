'''
import os

from dotenv import load_dotenv

print('settings')
# settings.py

#  ENV Variable 
ENV_ERROR = False # set to True when env variables are not set

load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# environment variable handler
from dotenv import load_dotenv
IMP_TABLE_NAME=os.getenv("IMP_TABLE_NAME")
IMP_TITLE=os.getenv("IMP_TITLE")
IMP_DESC=os.getenv("IMP_DESC")
GH_USER = os.getenv("GH_USER")
DW_USER = os.getenv("DW_USER")
DW_AUTH_TOKEN = os.getenv("DW_AUTH_TOKEN")

# GH_URL = os.getenv("GH_URL")
print('ENV')
print('DW_USER: ', os.getenv("DW_USER"))
# print('GH_USER: ', os.getenv("GH_USER"))
# print('DW_USER: ', os.getenv("DW_USER"))

if IMP_TABLE_NAME == None:
    ENV_ERROR = True
    
if IMP_TITLE == None:
    ENV_ERROR = True

if IMP_DESC == None:
    ENV_ERROR = True
            
if GH_USER == None:
    ENV_ERROR = True
    
if DW_USER == None:
    ENV_ERROR = True

if DW_AUTH_TOKEN == None:
    ENV_ERROR = True

#####################
##### Globals
#####################

GH_URL_RAW = None
GH_URL_CLEAN = None
DW_DB_URL = None

if not ENV_ERROR:
    GH_URL_RAW = "https://raw.githubusercontent.com/%s/data.world/master/raw-data/".replace("%s",os.getenv("GH_USER"))
    GH_URL_CLEAN = "https://raw.githubusercontent.com/%s/data.world/master/clean-data/".replace("%s",os.getenv("GH_USER"))
    DW_DB_URL = "https://api.data.world/v0/datasets/%s/".replace("%s", os.getenv("DW_USER"))



def main():
    assert GH_USER != None, ", Add GH_USER=<your-github-user-name> in a data.world/scripts/adopt-a-world/.env file?"
    assert DW_USER != None, ", Add DW_USER=<your-github-user-name> in a data.world/scripts/adopt-a-world/.env file?"
    assert DW_AUTH_TOKEN != None, ", Add DW_AUTH_TOKEN=<your-github-user-name> in a data.world/scripts/adopt-a-world/.env file?"


if __name__ == "__main__":
    # execute only if run as a script
    main()
'''