import os
from dotenv import load_dotenv
import sys
print('app', '{}/_lib'.format(os.getcwd()) )

sys.path.insert(0, '{}/_lib'.format(os.getcwd()))

load_dotenv()