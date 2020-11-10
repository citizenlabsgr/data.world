from process_load import ProcessLoad
import datadotworld as dw
import pandas as pd

class ProcessLoadDataWorld(ProcessLoad):
    '''
    creates a dataframe with a fresh copy of the data.world dataset
    dont forget to run
    '''
    def __init__(self, import_file_name):
        ProcessLoad.__init__(self ,import_file_name)
        self.summary_key ='01'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    # def get_dataframe(self):
    #    return self.dataframe

    def addColumns(self):
        if 'dr_discharge' not in self.dataframe.columns.values:
            self.dataframe['dr_discharge'] = self.dataframe['dr_subwatershed']

    def process(self):
        print('* ProcessLoad Data.World')
        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['name' ]= self.filename(self.import_file_name)
        self.getSummary()[self.get_class_key()]['before' ] =0
        '''
        import_file_name is the full path and name of import file
        returns the original raw data as pandas dataframe
        '''
        # download to ~/.dw/cache/{}/latest/data/grb_drains.csv
        print('self.import_file_name: ' + self.import_file_name)
        self.dataframe = dw.load_dataset(self.import_file_name, auto_update=True)
        #fstr = '~/.dw/cache/{}/latest/data/grb_drains.csv'.format('citizenlabs/grb-storm-drains-2019-04-03')
        fstr = '~/.dw/cache/{}/latest/data/lgrow_current.csv'.format('citizenlabs/lgrow-storm-drains-current')

        #
        self.dataframe = pd.read_csv(fstr)

        self.addColumns()

        for col in self.get_dataframe().columns.values:
            print( ' -- column:', col)

        # SUMMARIZE
        self.getSummary()[self.get_class_key()]['after' ]= len(self.dataframe)
        diff = self.getSummary()[self.get_class_key()]['after']  - self.getSummary()[self.get_class_key()]['before']
        self.getSummary()[self.get_class_key()]['diff'] = diff

def main():
    import os
    from dotenv import load_dotenv
    from util import Util
    load_dotenv()
    #dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'
    dw_source = 'citizenlabs/lgrow-storm-drains-current'

    #import_file_name = '_test_.csv'
    #sampleCSV = SampleCSV(import_file_name).run()
    # create a file
    #print(os.getenv("DW_AUTH_TOKEN"))

    load = ProcessLoadDataWorld(dw_source).run()
    print(load.get_class_key())
    assert load.get_class_key() == '01.ProcessLoadDataWorld'
    assert load.get_history_folder().endswith('data/_history')

    #assert load.isLoaded()

    #Util().deleteFile(os.getcwd(), import_file_name)

if __name__ == "__main__":
    main()
