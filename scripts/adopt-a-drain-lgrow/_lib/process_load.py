from process import Process
import os.path
from os import path
import csv
import pandas as pd

class ProcessLoad(Process):
    def __init__(self, import_file_name):
        Process.__init__(self)
        # import_file_name is  full local file name or url to source
        self.import_file_name = import_file_name
        self.dataframe = None

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def get_dataframe(self):
        return self.dataframe

    def isLoaded(self):
        rc = False
        #if path.exists('./history/{}.{}.ran'.format(self.getClassName(), self.filename(self.import_file_name))):
        if self.dataframe is not None:
            rc = True
        return rc

    def get_app_name(self):
        # returns application name from script path
        scripts_path = os.getcwd()
        rc = ''
        pth = scripts_path.split('/')
        rc = pth[len(pth) - 1]
        if rc == '_lib':
            rc = pth[len(pth) - 2]
        return rc

    def diagram(self):
        print('''
          [Sample] <--- +
             |          ^
             |          |
          (datum) ----> +
             |

          ''')

    def process(self):
        self.diagram()
        if not self.isLoaded():
            self.dataframe = pd.read_csv(self.import_file_name)
        else:
            print('Already loaded')


def main():
    from sample_csv import SampleCSV
    from util import Util

    import_file_name = '_raw_.csv'
    #sampleCSV = SampleCSV(import_file_name).run()
    sampleCSV = SampleCSV().write()

    # create a file
    load = ProcessLoad(import_file_name).run()
    assert load.isLoaded()
    assert load.get_app_name() == 'adopt-a-drain-lgrow'

    #print('history ' + load.get_history_folder())
    #assert load.get_history_folder().endswith('data/_history')

    #Util().deleteFile(os.getcwd(), import_file_name)
    sampleCSV.delete()

if __name__ == "__main__":
    main()