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
import copy

# ProcessWrangle( maps, expected_output_columns_list)

class ProcessWrangle(Process):
    def __init__(self, loadDataWorld):
        Process.__init__(self)
        # self.report = {}
        self.setSummaryNo('02')
        self.concat_list=[]
        self.datasetList = [loadDataWorld.import_file_name]
        #print('####### LOAD DW 02')
        self.concat_list.append(loadDataWorld.get_dataframe()) # start stacking datasets
        # print('count concat_list ', len(loadDataWorld.get_dataframe()))
        #print('A concat_list ', len(self.concat_list) , len(self.concat_list[len(self.concat_list)-1]))
        # self.report= {}
        # self.report['dataworld'] = {'beginCount': len(loadDataWorld.get_dataframe())}

        self.maps = {
                      "commonNameMap": ConfigCommonNameMap(),
                      "region_map": ConfigRegionMap()
                    }
        #self.expected_output_columns_list = expected_output_columns_list
        self.expected_output_columns_list = ConfigOutputColumns


    #def get_class_key(self):
    #    return '{}.{}'.format(self.summary_key, self.getClassName())

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
        rawFileList = [self.filename(f) for f in Helper().get_raw_files()]
        convertedFileList = ['{}.csv'.format(self.filename(f)) for f in Helper().get_raw_files()]

        for file in Helper().get_raw_files():

            if not file.endswith('.csv'):
                #self.addPath('''
                #|                 + x<--- [Convert to CSV] <--- ({}).csv <--- ({})'''.format(self.filename(file),self.filename(file)))
                self.xls2csv(file)


    def conversion(self, sourceFile):
        if not sourceFile.endswith('.csv'):
            self.xls2csv(sourceFile)

    def process(self):
        #print('Dataset ', self.datasetList)

        rawFileList = [self.filename(f) for f in Helper().get_raw_files()]
        convertedFileList = ['{}.csv'.format(self.filename(f)) for f in Helper().get_raw_files()]

        #self.addPath('''
        #(raw: {})
        #    |
        #[Convert Raw Data Files to CSV]
        #    |
        #(converted: {})
        #|'''.format(rawFileList, convertedFileList))
        #print('* ProcessWrangle x')
        # file_names = ['dw']
        # print('self.get_class_key()', self.get_class_key())
        # self.getSummary()[self.get_class_key()]={}
        # self.getSummary()[self.get_class_key()]['before']=0

        # get list of raw data files
        # print(' - raw folder ', Helper().get_raw_data_folder())
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
        #self.addPath('''
        #[Process New Data] <-------- +  source: {}
        #|                         | '''.format(self.getClassName()))
        #self.conversions()  # convert excel files to csv

        # load up the files in the raw data folder
        # for in_f in Helper().get_csv_files():
        for in_f_raw in Helper().get_raw_files():

            # convert to csv
            self.conversion(in_f_raw)
            #self.addPath('''
            #      |                 + <--- [Convert to CSV] <--- ({}).csv <--- ({})'''.format(self.filename(in_f),
            #                                                                                  self.filename(in_f)))
            in_f = '{}.csv'.format(in_f_raw)
            # skip files that have already run
            loadDrains = ProcessLoadDrains(in_f)

            if not loadDrains.isLoaded():
                # print('####### LOAD DRAINS 02')

                # LOAD CSV

                loadDrains \
                    .addPath('''
       |                    |
    [Process Raw Data]      |     source: {}
       |                    |
       |                    + --- [Convert to CSV] <--- ({}) <--- ({})'''.format(self.getClassName(),self.filename(in_f),self.filename(in_f_raw))) \
                    .run()  # b
                self.appendPath(loadDrains.getPath())
                self.datasetList.append(self.filename(in_f))
                self.getSummary()[loadDrains.filename(in_f)] = {}
                self.getSummary()[loadDrains.filename(in_f)][loadDrains.get_class_key()]=loadDrains.getSummary()[loadDrains.get_class_key()]

                # CLEAN

                cleanDrains = ProcessCleanDrains(loadDrains) \
                    .run()  # c
                self.appendPath(cleanDrains.getPath())
                self.getSummary()[loadDrains.filename(in_f)][cleanDrains.get_class_key()] = cleanDrains.getSummary()[cleanDrains.get_class_key()]

                self.set_dataframe(cleanDrains.get_dataframe())

                # CONDENCE individual datasets

                rowCondense = ProcessCondenseRows(cleanDrains) \
                    .addPath('''
       |                    + -- +    
       |                         | 
    [Condense Dataset Rows]      |     source: {}
       |                         |'''.format('ProcessCondenseRows')) \
                    .run()  # d
                self.appendPath(rowCondense.getPath())

                self.getSummary()[loadDrains.filename(in_f)][rowCondense.get_class_key()] = rowCondense.getSummary()[rowCondense.get_class_key()]

                self.set_dataframe(rowCondense.get_dataframe())
               # CONDENSE COLUMNS

                colCondense = ProcessCondenseColumns(rowCondense) \
                    .addPath('''
       |                         | 
    [Condense Dataset Cols]      |     source: {}
       |                         |'''.format('ProcessCondenseColumns')) \
                    .run()  # d
                self.appendPath(colCondense.getPath())

                self.getSummary()[loadDrains.filename(in_f)][colCondense.get_class_key()] = colCondense.getSummary()[colCondense.get_class_key()]

                self.set_dataframe(colCondense.get_dataframe())
                # print('   condensed cols to ', len(self.get_dataframe().columns))

                # COMPILE
                self.addPath('''  
       |                    |         
       |                 ({})           
       |                    |        
    [Compile Data]          |      source: {}
       |                    | 
       |                    + <--- ({})'''.format(loadDrains.filename(in_f),self.getClassName(), ' + '.join( self.datasetList)))
                #print('####### COMPILE DRAINS')
                self.concat_list.append(self.get_dataframe())
                #print('B concat_list ', len(self.concat_list))
                #print('B concat_list ', len(self.concat_list), len(self.concat_list[len(self.concat_list) - 1]))

                #self.report[loadDrains.filename(in_f)]['endCount'] = len(colCondense.get_dataframe())

        #print('report', self.report)
        self.addPath(''' 
       |                    |            
       |                 (compilied-data) -----> +  
       |                                         |
    [Combine Datasets]                           |        source: {}                              
       |                                         |'''.format(self.getClassName()))

        for i in self.datasetList:
            self.addPath('''
       |                                         + <--- ({}) '''.format(i))
        self.addPath('''
       |                                         |
       |                         + <--------- (combined-dataset)   ''')
        '''
        --------------------------------- combine datasets
        datasets are big chunks of data that need to be broken down
        '''


        #print('A dataframe ',len(self.get_dataframe()))
        self.set_dataframe(pd.concat(self.concat_list))
        #print('B dataframe ',len(self.get_dataframe()))

        #self.report['dataworld']['combinationCount'] = len(self.get_dataframe())

        '''
        --------------------------------- ProcessCondense dataset (cols, rows)
        '''

        # self.getSummary()[self.get_class_key()]['before']=len(self.get_dataframe())
        #             .setSummary(self.getSummary()) \
        #print('####### CONDENSE ALL 05')

        condense = ProcessCondense(self.get_dataframe(),ConfigOutputColumns(), ConfigTemporaryColumnList(), ConfigOutlierSettings()) \
            .addPath('''     
       |                         |
    [Condense Combined]          |    source: {}
       |                         |'''.format('ProcessCondense')) \
            .run()  # e
        self.appendPath(condense.getPath())
        #self.report['dataworld']['condenseCount'] = len(condense.get_dataframe())

        self.set_dataframe(condense.get_dataframe())
        #print('C dataframe ',len(self.get_dataframe()))

        # print('  condenced ', len(condense.get_dataframe()))
        #self.report['dataworld']['endCount'] = len(self.get_dataframe())

        #print(''.join(self.processPath))

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