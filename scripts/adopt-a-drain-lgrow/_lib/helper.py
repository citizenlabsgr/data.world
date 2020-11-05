import os
import datetime
import pandas as pd
#from lib.p3_Process Logger import Process Logger
#from util_process logger import Process Logger
from util import Util
from datetime import date

class Helper():
    def __init__(self):
        self.ext_list=['xlsx','xls']
        self.current_name = 'current.csv'
        self.watershed='lgrow' # lower grand river organization of watersheds

    def get_csv_files(self):
        # return all filess in folders under /_raw/<community-name>

        file_list = []
        # process folders
        for folder in self.get_community_folders():
            # load up csv filenames
            for file in Util().getFileList(folder, 'csv'):
                file_list.append('{}/{}'.format(folder, file))

        return file_list

    def get_raw_files(self):
        # return all filess in folders under /_raw/<community-name>
        # return all filess in folders under /_raw/<community-name>

        file_list = []
        for folder in self.get_community_folders():
            for ext in self.ext_list:
                for file in Util().getFileList(folder, ext):
                    file_list.append('{}/{}'.format(folder, file))

        return file_list

    def get_raw_data_folder(self):
        '''
        returns path to raw data from script path
        '''
        scripts_path = os.getcwd()
        #return '{}/{}/data/_raw'.format(self.get_repo_folder(), Helper().get_app_name() )
        # data.world/raw-data/adopt-a-drain-lgrow
        return '{}/raw-data/{}'.format(self.get_repo_folder(), Helper().get_app_name() )

    def get_community_folders(self):
        # return list of folders under /data/_raw
        return Util().getFolderList(self.get_raw_data_folder())

    def get_app_name(self):

        # returns application name from script path

        scripts_path = os.getcwd()
        rc = ''
        pth = scripts_path.split('/')
        rc = pth[len(pth) - 1]
        if rc == '_lib':
            rc = pth[len(pth) - 2]
        return rc


    def get_clean_data_folder(self):
        '''
        returns path to clean data from script path
        '''
        scripts_path = os.getcwd()
        rc = self.get_repo_folder() + '/clean-data/' + Helper().get_app_name()
        if not os.path.exists(rc):
            os.makedirs(rc)
        return rc

    def get_repo_folder(self):

        # returns path to the repo folder from script path

        scripts_path = os.getcwd()
        rc = ''
        rc = scripts_path.replace('/' + Helper().get_app_name(), '') \
            .replace('/scripts', '') \
            .replace('/' + '_lib', '')
        return rc

    def get_current_name(self):
        return '{}-{}'.format(self.watershed, self.current_name)

    def get_version_name(self):
        return '{}-{}.csv'.format(self.watershed, self.get_version())

    def get_version(self):
        now = date.today()
        return now.strftime('%Y-%m-%d')

    def get_history_folder(self):
        return '{}/history'.format(self.get_repo_folder())

def main():
    from util import Util
    helper = Helper()
    print('--------------------------')
    print(helper.get_repo_folder())
    assert helper.get_repo_folder().endswith('data.world')

    print('get_app_name: ', helper.get_app_name())
    assert helper.get_app_name()=='adopt-a-drain-lgrow'

    #data.world/raw-data/adopt-a-drain-lgrow
    print(helper.get_raw_data_folder())
    #assert helper.get_raw_data_folder().endswith('_raw')
    assert helper.get_raw_data_folder().endswith(helper.get_app_name())

    print('get_community_folders: ', helper.get_community_folders())
    assert len(helper.get_community_folders()) > 0

    print('get_raw_files: ',helper.get_raw_files())
    assert len(helper.get_raw_files()) > 0

    print('get_history_folder: ', helper.get_history_folder())
    assert Util().folder_exists(helper.get_history_folder())

    print('get_csv_files: ',helper.get_csv_files())
    #assert len(helper.get_csv_files()) > 0

    print ('get_clean_data_folder: ', helper.get_clean_data_folder())
    print(helper.get_current_name())
    print(helper.get_version_name())


if __name__ == "__main__":
    main()


'''
def exportMaintainerConfig(gh_file_name, gh_file_type, dw_title, dw_desc, dw_table_name):

    #write variables to file, used by maintainer in 02.Prod.Process.ipynb
    #outputs: maintainer-config.json

    maintainer_config = '"gh_file_name": "{}", "gh_file_type": "{}", "dw_title": "{}", "dw_desc": "{}", "dw_table_name": "{}"'
    maintainer_config = maintainer_config.format(gh_file_name, gh_file_type, dw_title, dw_desc, dw_table_name )
    maintainer_config = '{' + maintainer_config + '}'
    
    mantainer_config_file = Process Logger('./maintainer/maintainer-config.json')
    mantainer_config_file.kill()
    mantainer_config_file.log(maintainer_config) 

def get_file_name(path_file):
    #scripts_path = os.getcwd()
    rc = ''
    pth = path_file.split('/')
    rc = pth[len(pth) - 1]
    return rc

def get_app_name():

    #returns application name from script path

    scripts_path = os.getcwd()
    rc = ''
    pth = scripts_path.split('/')
    rc = pth[len(pth)-1]
    return rc 
# cell_log.collect('* get_repo_folder( script_folder_name )')
def get_repo_folder():

    # returns path to the repo folder from script path

    scripts_path = os.getcwd()
    rc = ''
    rc = scripts_path.replace('/' + get_app_name(), '').replace('/scripts','')
    return rc
# cell_log.collect('* get_raw_data_folder( script_folder_name )')
def get_raw_data_folder():

    # returns path to raw data from script path

    scripts_path = os.getcwd()
    return get_repo_folder() + '/raw-data/' + get_app_name()
# extra files users and basin_users

# return a list of raw data file names
def get_raw_files(ext):
    file_list = ['{}/{}'.format(get_raw_data_folder(),fn) for fn in os.listdir(get_raw_data_folder()) if fn.endswith(ext)]
    return file_list

# cell_log.collect('* get_clean_data_folder( script_folder_name )')    
def get_clean_data_folder():

    # returns path to clean data from script path

    scripts_path = os.getcwd()
    rc = get_repo_folder() + '/clean-data/' + get_app_name()
    if not os.path.exists(rc):
        os.makedirs(rc)
    return rc

def get_test_version_folder():

    #returns path to test subfolder of clean data from script path

    scripts_path = os.getcwd()
    rc = get_repo_folder() + '/test-data/' + get_app_name() 
    if not os.path.exists(rc):
        os.makedirs(rc)
    return rc

def get_clean_file(raw_file_name):
    rc = raw_file_name.replace(get_raw_data_folder(), get_clean_data_folder())
    return rc



def get_raw_file_name():

    #get list of files in clean-data folder
    #return the first name

    rc = ''
    ls = os.listdir(get_raw_data_folder())
    for f in ls:
        rc = f
    return rc
    

def open_csv(path_file):
    if not os.path.isfile( path_file ):
        raise Exception('CSV not found at {}'.format(path_file))
        
    return pd.read_csv( path_file )

def open_raw_data(local_config):

    #returns the original raw data as pandas dataframe

    return pd.read_csv(local_config["local_raw"])

def get_temp_password():
    return 'aA1!aaaa'


def get_daystamp():

    #   get current day
    #   format a yyyy-mm-dd

    
    dt = datetime.datetime.now()
    m = '{}'.format(dt.month)
    d = '0{}'.format(dt.day)
    if dt.month < 10:
        m = '0{}'.format(dt.month)
    if dt.day < 10:
        d = '0{}'.format(dt.day)

    rc = '{}-{}-{}'.format(dt.year, m, d )
    return rc 
'''
