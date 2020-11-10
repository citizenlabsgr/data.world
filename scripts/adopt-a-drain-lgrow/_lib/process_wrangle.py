from process import Process
import csv
import pandas as pd
#import os
#from output_drains import ProcessOutputDrains
from config_outlier_settings import ConfigOutlierSettings
from process_load_dataworld_patch_20190927 import ProcessLoadDataworldPatch20190927
from process_load_drains import ProcessLoadDrains

from process_clean_drains import ProcessCleanDrains
from process_condense import ProcessCondense
from process_condense_row import ProcessCondenseRows
from process_condense_col import ProcessCondenseColumns
from config_output_columns import ConfigOutputColumns
from config_temporary_column_list import ConfigTemporaryColumnList
from config_common_name_map import ConfigCommonNameMap
from config_region_map import ConfigRegionMap
from helper import Helper

# ProcessWrangle( maps, expected_output_columns_list)

class ProcessWrangle(Process):
    def __init__(self, loadDataWorld):
        Process.__init__(self)
        self.concat_list=[]
        print('####### LOAD DW 01')
        self.concat_list.append(loadDataWorld.get_dataframe())

        #self.set_dataframe(load.get_dataframe())
        self.maps = {
                      "commonNameMap": ConfigCommonNameMap(),
                      "region_map": ConfigRegionMap()
                    }
        #self.expected_output_columns_list = expected_output_columns_list
        self.expected_output_columns_list = ConfigOutputColumns

        self.summary_key = '00'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def xls2csv(self, xls_name):
        import xlrd
        # generates a csv file from the first sheet in an excel file

        wb = xlrd.open_workbook(xls_name,formatting_info=True) # formatting_info=True keeps blanks in data
        sh = wb.sheet_by_index(0)
        your_csv_file = open('{}.csv'.format(xls_name), 'w', encoding='utf8')

        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
        for rownum in range(sh.nrows):
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()

    def filename(self, in_f):
        ps = in_f.split('/')
        return ps[len(ps) - 1]

    def conversions(self):
        for file in Helper().get_raw_files():
            print(' -- convert ', file)
            if not file.endswith('.csv'):
                self.xls2csv(file)
        '''
        for xls in Helper().get_raw_files('xls'):
            print(' -- convert ', xls)
            self.xls2csv(xls)
        for xlsx in Helper().get_raw_files('xlsx'):
            print(' -- convert ', xlsx)
            self.xls2csv(xlsx)
        '''
    '''        
    def finalCSV(self):

        self.get_dataframe().to_csv(local_config["local_clean"], index=False)
    '''

    def process(self):
        print('* ProcessWrangle')

        print('self.get_class_key()', self.get_class_key())
        # self.getSummary()[self.get_class_key()]={}
        # self.getSummary()[self.get_class_key()]['before']=0

        # get list of raw data files
        print(' - raw folder ', Helper().get_raw_data_folder())
        # print(Helper().get_raw_files('csv'))
        raw_folder = Helper().get_raw_data_folder()
        clean_folder = Helper().get_clean_data_folder()

        #concat_list = []
        # * load data
        # * convert xls to csv
        # * fix column names
        # * map expected colums to raw-data columns
        # * drop drains without a facility id
        # * fix column types

        self.conversions()  # convert excel files to csv
        '''
        #print('####### LOAD DW 01')
        # load these up first
        
        loadDataWorld = ProcessLoadDataworldPatch20190927(dw_source)

        loadDataWorld \
            .setSummary(self.getSummary()) \
            .run()  # a
        concat_list.append(loadDataWorld.get_dataframe())
        '''

        # load up the files in the raw data folder
        for in_f in Helper().get_csv_files():
            # print(' - raw: ', self.filename(in_f))

            # skip files that have already run
            loadDrains = ProcessLoadDrains(in_f)
            if not loadDrains.isLoaded():
                print('####### LOAD DRAINS 02')

                # LOAD
                # loadDrains = ProcessLoadDrains(in_f)\
                loadDrains \
                    .setSummary(self.getSummary()) \
                    .run()  # b

                self.set_dataframe(loadDrains.get_dataframe())

                # CLEAN
                print('####### CLEAN DRAINS 03')
                cleanDrains = ProcessCleanDrains(loadDrains) \
                    .setSummary(self.getSummary()) \
                    .run()  # c
                '''
                cleanDrains = ProcessCleanDrains(self.get_dataframe(),
                                          self.maps['commonNameMap'],
                                          self.maps['region_map']) \
                    .setSummary(self.getSummary()) \
                    .run()  # c
                '''
                self.set_dataframe(cleanDrains.get_dataframe())

                # CONDENCE individual datasets
                print('####### ROWCONDENCE DRAINS 04')

                rowCondense = ProcessCondenseRows(cleanDrains) \
                    .setSummary(self.getSummary()) \
                    .run()  # d

                self.set_dataframe(rowCondense.get_dataframe())

                print('####### COLCONDENCE DRAINS 04')

                colCondense = ProcessCondenseColumns(rowCondense) \
                    .setSummary(self.getSummary()) \
                    .run()  # d

                self.set_dataframe(colCondense.get_dataframe())

                # COMPILE
                print('####### COMPILE DRAINS')
                self.concat_list.append(self.get_dataframe())

        '''
        --------------------------------- combine datasets
        '''
        print('concat_list', len(self.concat_list))
        for ds in self.concat_list:
            print('df cnt', len(ds))

        self.set_dataframe(pd.concat(self.concat_list))

        '''
        --------------------------------- ProcessCondense dataset (cols, rows)
        '''

        # self.getSummary()[self.get_class_key()]['before']=len(self.get_dataframe())

        print('####### CONDENSE ALL 05')

        condense = ProcessCondense(self.get_dataframe(),ConfigOutputColumns(), ConfigTemporaryColumnList(), ConfigOutlierSettings()) \
            .setSummary(self.getSummary()) \
            .run()  # e

        self.set_dataframe(condense.get_dataframe())

        '''
        --------------------------------- save csv 
        '''
        '''
        # assume new file and remove old one
        local_config["local_clean"] = '{}/{}'.format(Helper().get_clean_data_folder(), metadata['output_file_name'])

        if os.path.isfile(local_config["local_clean"]):
            os.remove(local_config['local_clean'])
            #cell_log.collect('* deleted {} '.format(local_config['local_clean']))

        # self.getSummary()[self.get_class_key()]['after']=len(self.get_dataframe())
        # diff = self.getSummary()[self.get_class_key()]['after']  - self.getSummary()[self.get_class_key()]['before']
        # self.getSummary()[self.get_class_key()]['diff'] = diff

        #pprint(self.getSummary())

        # stop if columns are not expected
        # self.validateOutputColumns()

        # self.finalCSV()
        # df_source.to_csv(local_config["local_clean"], index=False)
        ProcessOutputDrains(self.get_dataframe(), self.expected_output_columns_list).run()
        '''
def main():
    # dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'
    dw_source = 'citizenlabs/lgrow-storm-drains-current'
    loadDataWorld = ProcessLoadDataworldPatch20190927(dw_source).run()
    wrangle = ProcessWrangle(loadDataWorld).run()

if __name__ == "__main__":
    main()