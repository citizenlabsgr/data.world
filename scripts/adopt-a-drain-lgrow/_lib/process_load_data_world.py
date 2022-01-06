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
        self.setSummaryNo('01')

    def addColumns(self):
        if 'dr_discharge' not in self.dataframe.columns.values:
            self.dataframe['dr_discharge'] = self.dataframe['dr_subwatershed']

    def process(self):
        #self.diagram()
        # print('* ProcessLoad Data.World')
        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['before'] =0
        '''
        import_file_name is the full path and name of import file
        returns the original raw data as pandas dataframe
        '''
        # download to ~/.dw/cache/{}/latest/data/grb_drains.csv
        self.dataframe = dw.load_dataset(self.import_file_name, auto_update=True)

        fstr = '~/.dw/cache/{}/latest/data/lgrow_current.csv'.format('citizenlabs/lgrow-storm-drains-current')

        #
        self.dataframe = pd.read_csv(fstr)

        self.addColumns()
        cols = 'columns: '
        for col in self.get_dataframe().columns.values:
            cols += col + ', '

        self.addPath('''
    Overview                           Details   
    --------                           -------
                                       ({})
                                          |
    [Retrieve Production Dataset]         |     source: {} 
       |                                  |
       |                               [Get Data from DataWorld] (response.data: {})       
       |                                  |
    [Load Production Dataset]             |     source: {}                        
       |                                  |               
       |                               [Cache DW data] <--- ({})
       |                                  |        (production count: {})'''.format(self.import_file_name,self.getClassName(), cols, self.getClassName(), fstr, len(self.dataframe)))

        # SUMMARIZE
        self.getSummary()[self.get_class_key()]['after' ]= len(self.dataframe)

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
    # print(load.get_class_key())
    assert load.get_class_key() == '01.ProcessLoadDataWorld'
    assert load.get_history_folder().endswith('data/_history')

    #assert load.isLoaded()

    #Util().deleteFile(os.getcwd(), import_file_name)

if __name__ == "__main__":
    main()
