import os

from dotenv import load_dotenv

print('settings')
# settings.py

load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# environment variable handler
from dotenv import load_dotenv
# junk = os.getenv("junk")
# print('junk: ', junk, ", environment variable is not set. did you create it in a .env file?")


DW_USER = os.getenv("DW_USER")
GH_URL = os.getenv("GH_URL")
DW_DB_URL = os.getenv("DW_DB_URL")
DW_AUTH_TOKEN = os.getenv("DW_AUTH_TOKEN")
# DW_DB_RW_TOKEN = os.getenv("DW_DB_RW_TOKEN")

assert DW_USER != None, ", environment variable is not set. did you create it in a .env file?"
# assert GH_URL != None, ", environment variable is not set. did you create it in a .env file?"
# assert DW_DB_URL != None, ", environment variable is not set. did you create it in a .env file?"
assert DW_AUTH_TOKEN != None, ", environment variable is not set. did you create it in a .env file?"
#assert DW_DB_RW_TOKEN != None, ", environment variable is not set. did you create it in a .env file?"


def main():
  assert junk != None


if __name__ == "__main__":
    # execute only if run as a script
    main()