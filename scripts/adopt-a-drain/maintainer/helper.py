import os
import pandas as pd
from lib.p3_ProcessLogger import ProcessLogger
'''
def exportMaintainerConfig(clean_file_name, ext, title, desc):
    
    # write variables to file, used by maintainer in 02.Prod.Process.ipynb 
    # outputs: maintainer-config.json
    
    maintainer_config = '"clean_name": "{}", "ext": "{}", "title": "{}", "desc": "{}"'
    maintainer_config = maintainer_config.format(clean_file_name, ext, title, desc)
    maintainer_config = '{' + maintainer_config + '}'
    
    mantainer_config_file = ProcessLogger('./maintainer/maintainer-config.json')
    mantainer_config_file.kill()
    mantainer_config_file.log(maintainer_config) 
'''

def get_app_name():
    '''
    returns application name from script path
    '''
    scripts_path = os.getcwd()
    rc = ''
    pth = scripts_path.split('/')
    
    rc = pth[len(pth)-2]
    return rc 
# cell_log.collect('* get_repo_folder( script_folder_name )')
def get_repo_folder():
    '''
    returns path to the repo folder from script path
    '''
    scripts_path = os.getcwd()
    rc = ''
    rc = scripts_path.replace('/' + get_app_name(), '').replace('/scripts','')
    return rc
# cell_log.collect('* get_raw_data_folder( script_folder_name )')
def get_raw_data_folder():
    '''
    returns path to raw data from script path
    '''
    scripts_path = os.getcwd()
    return get_repo_folder() + '/raw-data/' + get_app_name()
# cell_log.collect('* get_clean_data_folder( script_folder_name )')    
def get_clean_data_folder():
    '''
    returns path to clean data from script path
    '''
    scripts_path = os.getcwd()
    rc = get_repo_folder() + '/clean-data/' + get_app_name()
    if not os.path.exists(rc):
        os.makedirs(rc)
    return rc
def get_raw_file_name():
    '''
    get list of files in clean-data folder 
    return the first name
    '''
    rc = ''
    ls = os.listdir(get_raw_data_folder())
    for f in ls:
        rc = f
    return rc
    
# print('raw_data: ', getRawFileName(os.getcwd()))

def open_raw_data(local_config):
    '''
    returns the original raw data as pandas dataframe
    '''
    return pd.read_csv(local_config["local_raw"])

