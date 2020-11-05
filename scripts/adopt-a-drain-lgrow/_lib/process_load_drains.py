from process_load import ProcessLoad
# from util_process logger import Process Logger
from sample_csv import SampleCSV
from helper import Helper
import os
import json
import pandas as pd

class ProcessLoadDrains(ProcessLoad):

    def __init__(self, import_file_name):
        ProcessLoad.__init__(self ,import_file_name)
        # self.import_file_name=import_file_name
        self.summary_key ='02'
        #self.logger = Process Logger \
        #    ('./history/{}.{}.ran'.format(self.getClassName() ,self.filename(self.import_file_name) ))

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    '''
    def get_app_name(self):
        
        #returns application name from script path
        
        scripts_path = os.getcwd()
        rc = ''
        pth = scripts_path.split('/')
        rc = pth[len(pth ) -1]
        if rc == '_lib':
            rc = pth[len(pth) -2]
        return rc
    '''
    '''
    def get_repo_folder(self):
        
        #returns path to the repo folder from script path
        
        scripts_path = os.getcwd()
        rc = ''
        rc = scripts_path.replace('/' + Helper().get_app_name(), '')\
            .replace('/scripts' ,'')\
            .replace('/'+ '_lib','')
        return rc
    '''
    '''
    def get_raw_data_folder(self):
        
        #returns path to raw data from script path
        
        scripts_path = os.getcwd()
        # return self.get_repo_folder() + '/raw-data/' + Helper().get_app_name()
        return '{}/{}/data/_raw'.format(self.get_repo_folder(), Helper().get_app_name() )
    '''
    def filename(self, in_f):
        ps = in_f.split('/')
        return ps[len(ps ) -1]

    def process(self):
        print('* ProcessLoad Drains', self.filename(self.import_file_name))

        # if path.exists('./history/{}.{}.ran'.format(self.getClassName(),self.filename(self.import_file_name) )):
        if self.isLoaded():
            print('Already ran {}...skipping'.format(self.import_file_name))
            self.getSummary()[self.get_class_key() ] ={}
            self.getSummary()[self.get_class_key()]['name' ]= self.filename(self.import_file_name)
            self.getSummary()[self.get_class_key()]['status' ] ='skipped'
            return

        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['name' ]= self.filename(self.import_file_name)
        self.getSummary()[self.get_class_key()]['before' ] =0

        '''
        import_file_name is the full path and name of import file
        returns the original raw data as pandas dataframe
        '''

        self.dataframe = pd.read_csv(self.import_file_name)

        # if 'load' not in self.getSummary():
        #    self.getSummary()['load']=[]


        self.getSummary()[self.get_class_key()]['after' ]= len(self.dataframe)
        # self.getSummary()['load'].append({'name': self.filename(self.import_file_name), 'records': len(self.dataframe)})
        diff = self.getSummary()[self.get_class_key()]['after']  - self.getSummary()[self.get_class_key()]['before']
        self.getSummary()[self.get_class_key()]['diff'] = diff
        self.getSummary()[self.get_class_key()]['status' ] ='loaded'
        # log the process
        #self.getLogger().log(json.dumps(self.getSummary()))

def main():
    from util import Util

    # create a file
    sampleCSV = SampleCSV().write()

    load = ProcessLoadDrains(sampleCSV.getFileName()).run()

    assert load.get_class_key() == '02.ProcessLoadDrains'
    assert load.getSummary() == {'02.ProcessLoadDrains': {'name': '_raw_.csv', 'before': 0, 'after': 3, 'diff': 3, 'status': 'loaded'}}
    # clean up
    sampleCSV.delete()

if __name__ == "__main__":
    main()