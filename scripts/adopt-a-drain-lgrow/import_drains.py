'''
Project: Adopt a Drain Data
    Author: James Wilfong, wilfongjt@gmail.com
Goals
    Merge drains from multiple communities across the watershed
    Resolve dataset conflicts i.e., drain identifyer uniqueness, data type, column names, and value range.
Limits
    ProcessOutputs from this script need to be manually pushed to the data.world repository (repo)
    Doesn't handle deleted drains
Assumptions
    Assume the community-dataset is a subset of all drains in the universe ;)
    Assume record identifiers are not unique across communities
    Assume the community-dataset's column names are not the same across communities
    Assume the community-dataset's data types are not the same across communities
    Assume the community-dataset's data-values ranges are not the same across communities
    Assume the community-dataset has duplicate records
    Assume the community-dataset's format is Comma Seperated Values (CSV) or Excel.
Inputs
    The current live dataset is downloaded from data.world
    Updates are put into the raw-data/adopt-a-drain of the data.world repo.
Process
    The process is initiated by running this Jupyter Notebook.
    load current drains dataset from data.world
    load dataset(s) from raw-data/adopt-a-drain folder
    clean data: create unique id from facility id etal.
    clean data: remove characters from facility ids
    clean data: map input columns to expected output columns
    clean data: fix common data problems
    condense data: remove drains with no facility id
    condense data: remove unneeded columns
    condense data: remove outliers
    condense: merge dataworld and new data
    condense data: remove duplicate drains (keep the first duplicate)
    concat: Make one big dataset from one or many
ProcessOutputs
    ProcessClean data is output to the clean-data/adopt-a-drain folder.
    save big dataset to clean-data/adopt-a-drain/grb_drains.csv
    save big dataset to clean-data/grb_drains-2019-08-020.csv
Next Steps
    Push updates to repo
    Sync data from github to dataworld
    Sync Manually
    or Wait for the weekly auto-sync
    Update the Adopt a Drain database
    Run Ruby rake process in Heroku

Process Steps
* convert excel files to csv
* download copy of dataworld data (patch)
* append dataworld data into empty dataframe
* get list of raw data files
* skip files that have already been run
* ProcessLoadDrains from raw data into dataframe
* CleanDrain
* CondenceRows
* CondenceColumns


[create local-store]
   |
[load DW data]            ProcessLoadDataworldPatch20190927
   |
[load raw data]           ProcessLoadDrains--->ProcessCleanDrains--->ProcessCondenseRows--->CondenseCol
   |
[store csv in repo]
   |
[commit repo]
   |
[Sync Data.World]
   |
[Update Adopt a Drain data-store]
   |
(done)

'''


import settings
#from IPython.display import display, HTML
#from IPython.display import Markdown
from config_common_name_map import ConfigCommonNameMap
from config_region_map import ConfigRegionMap
from config_temporary_column_list import ConfigTemporaryColumnList
from config_expected_columns_list import ConfigExpectedColumnsList
#from list_columns_expected import ListColumnsExpected
from config_output_columns import ConfigOutputColumns
from config_outlier_settings import ConfigOutlierSettings
# from util_processlogger import Process Logger

from helper import Helper

import os.path
from os import path
import sys
import time
import numpy as np
import pandas as pd
import csv # read and write csv files
from pprint import pprint
import os
import json
import datadotworld as dw
from shutil import copyfile

# import subprocess

# convenience functions -- cleaning
# cell_log.collect('* Import custom packages')
#from lib.p3_CellCounts import CellCounts
# import lib.p3_clean as clean

from util_configuration import get_configuration
import util_explore as explore

#import lib.p3_gather as gather # gathering functions
# import lib.p3_helper_functions as helper

import util_map as maps

from process_clean_drains import ProcessCleanDrains
from process_load_data_world import ProcessLoadDataWorld
from process_load_drains import ProcessLoadDrains
from config_common_name_map import ConfigCommonNameMap
from config_region_map import ConfigRegionMap


'''
    Input: CSV file in raw_data/ folder
    Process: clean (conform, condence)
    Output: is directed to the clean-data/ folder

    Name the output file using OUTPUT_FILE
    OUTPUT_FILELOCAL_CLEAN_NAME is used to name the data.world table
    Table names should start with letter, may contain letters, numbers, underscores

'''
'''
cell_log = Process Logger()
cell_log.clear()
table_name = 'lgrow_current'
'''

'''
    Assemble Names of:
        Application,
        Raw data file,
        ProcessClean data file
'''
'''
local_config = {
                 "app_name": Helper().get_app_name(),
                 "local_raw": None,
                 "local_clean": None
               }
'''
'''
    ------------- configure outliers
'''
# _outliers = {
#outlier_settings = ConfigOutlierSettings()
'''
ENV_ERROR=False
print("local_config ===========")
pprint(local_config)
print("outlier_settings ===========")
pprint(outlier_settings)
'''
'''
if ENV_ERROR:
    cell_log.collect("# Script Failure!!")
    cell_log.collect("# !!! Missing Environment Variables !!!")
    cell_log.collect("### see [Environment Variable Setup](#env-setup)")
'''
# common names from imported files and how then map to actual names

# if you add a temporary column, then add to this list remove before saving
#extraColumns = ConfigTemporaryColumnList()

#
#expected_process_columns_list=ConfigExpectedColumnsList()

# add column
#expected_output_columns_list=ConfigOutputColumns()

def main():
    from process_load_dataworld_patch_20190927 import ProcessLoadDataworldPatch20190927
    from process_wrangle import ProcessWrangle
    from process_output_drains import ProcessOutputDrains

    #dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'
    dw_source = 'citizenlabs/lgrow-storm-drains-current'

    output_name =  Helper().get_current_name()
    version_name = Helper().get_version_name()

    loadDataWorld = ProcessLoadDataworldPatch20190927(dw_source).run()
    wrangle = ProcessWrangle(loadDataWorld).run()
    current = ProcessOutputDrains(wrangle, output_name).run()
    history = ProcessOutputDrains(wrangle, version_name).run()

    # change the folder name and make production copy

if __name__ == "__main__":
    main()
