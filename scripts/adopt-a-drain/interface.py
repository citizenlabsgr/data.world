import subprocess
from datadotworld.client.api import RestApiError
import datadotworld as dw
import time

def github(df_source, tbl, cell_log):
    # print('* wrangle github')
    '''
            run git commands
    '''
    '''
        --------------------------------- GIT Process 
    '''
    cell_log.collect('')
    cell_log.collect('# GIT Process')
    '''
        --------------------------------- input
    '''
    cell_log.collect('* input: ' + tbl["local_clean"])
    '''
        --------------------------------- git add
    '''
    raw_folder = '../../raw-data'
    clean_folder = '../../clean-data'
    scripts_folder = '../../scripts'
    readme = '../../README.md'
    git_target_folder_list = [raw_folder,clean_folder,scripts_folder,readme]
    # execute git commands
    for target in git_target_folder_list:
        cell_log.collect('* git add {} -A'.format(target))
        output = subprocess.check_output(["git", "add", target ,"-A"])

    # --------------------------------- git commit

    cell_log.collect('* git commit -m "update raw-data, clean-data, and scripts"' )

    try:
        output = subprocess.check_output(["git", "commit", "-m", "'update raw-data, clean-data, and script files'"])
    except subprocess.CalledProcessError as error:
        print(error)
    except:
        cell_log.collect('* unknown error' )

        # --------------------------------- git push
        cell_log.collect('* git push origin ' + repo_branch)
        output = subprocess.check_output(["git", "push", "origin", repo_branch])


    

def data_world(df_source, tbl, cell_log):
    
    '''
    --------------------------------- Data World Process 
    run import to data.word
    '''
    # print('* wrangle data world')
    
    cell_log.collect('')
    cell_log.collect('# Data.World Process')
    cell_log.collect('* input: {}'.format(tbl["gh_url"] + ".csv") )
    cell_log.collect('* load: {} observations'.format(len(df_source)))

    try:
        deleteDataWorld(tbl)
        cell_log.collect('* drop: {}'.format(tbl["dw_dataset_id"]))
    except RestApiError as ex:
        print(' ' )
        # cell_log.collect('* No need to drop {}'.format(tbl["dw_dataset_id"]))

    del_delay = 6
    time.sleep(del_delay)

    try:
        cell_log.collect('* delay: {} seconds to delete data'.format(del_delay))
        loadDataWorld(tbl)
        cell_log.collect('* load: complete')
        cell_log.collect('* output: {}'.format(tbl["dw_url"] ))

    except RestApiError as ex:
        print('RestApiException create: ' + str(ex) )
        cell_log.collect('* LOAD FAIL: {}'.format(str(ex)))

    
def deleteDataWorld(tbl_def):
    '''
    Removes table from data.world
    tbl_def is { "owner_id": DW_USER, 
                     "dw_title": table_name, 
                     "gh_url": GH_URL + table_name, 
                     "visibility": "OPEN", 
                     "license": "Public Domain",
                     "files": {table_name + '.csv': {"url": GH_URL + table_name + '.csv'}},
                     "dw_url": DW_DB_URL + table_name + '.csv',
                     "dataset_id": DW_USER + "/" + table_name
                    }
    '''
    
    dw.api_client().delete_dataset(       
        tbl_def["dw_dataset_id"]
    )
        

def loadDataWorld(tbl_def):
    '''
        Takes a csv file and imports it into dataworld
        tbl_def is { "owner_id": DW_USER, 
                     "dw_title": table_name, 
                     "gh_url": GH_URL + table_name, 
                     "visibility": "OPEN", 
                     "license": "Public Domain",
                     "files": {table_name + '.csv': {"url": GH_URL + table_name + '.csv'}},
                     "dw_url": DW_DB_URL + table_name + '.csv' 
                    }
                    
    '''
    # api_client.create_dataset(
    dw.api_client().create_dataset(    
        owner_id=tbl_def["owner_id"], 
        title=tbl_def["dw_title"], 
        description=tbl_def["dw_desc"],
        visibility=tbl_def["visibility"],
        license=tbl_def['license'],
        files=tbl_def["files"]
    )
