from process_load_data_world import ProcessLoadDataWorld
from helper import Helper
from os import path
import os

class ProcessLoadDataworldPatch20190927(ProcessLoadDataWorld):
    '''
    Fill in blank dr_jurisdiction values with dr_owner in data.world

    * Unsure what caused the missing dr_jurisdictions
    * This patch was run only once on 09-27-2019
    * This patch affects the dataworld file citizenlabs/grb-storm-drains-2019-04-03
    * A record of this patch can be found in Patch20190927.ran
    * Patch will not run if ProcessLoadDataworldPatch20190927.ran is found in history/Patch20190927.ran

    '''
    def __init__(self, import_file_name):
        ProcessLoadDataWorld.__init__(self, import_file_name)
        self.summary_key ='01'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def process(self):
        super().process()
        # self.getLogger().kill()
        # skip if already run

        history_file = '{}/{}.ran'.format(Helper().get_history_folder(), self.getClassName())
        if path.exists(history_file):
            print('Already ran {}...skipping'.format(self.getClassName()))
            self.getSummary()[self.get_class_key() ] ={}
            self.getSummary()[self.get_class_key()]['name' ]= self.filename(self.import_file_name)
            self.getSummary()[self.get_class_key()]['status' ] ="skipped"
            return

        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['name' ]= self.filename(self.import_file_name)
        self.getSummary()[self.get_class_key()]['status' ] ="processed"
        self.getSummary()[self.get_class_key()]['before' ] =len(self.get_dataframe())

        print('ProcessLoadDataworldPatch20190927', len(self.get_dataframe()))
        # patch up blanck jurisdiction names with owner
        print(' -- replace dr_jurisdiction with dr_owner')
        self.get_dataframe()['dr_jurisdiction'] = self.get_dataframe()['dr_owner'] # is what it is

        # self.set_dataframe(data)
        # print(self.get_dataframe())
        self.getSummary()[self.get_class_key()]['after' ] =len(self.get_dataframe())
        diff = self.getSummary()[self.get_class_key()]['after']  - self.getSummary()[self.get_class_key()]['before']
        self.getSummary()[self.get_class_key()]['diff'] = diff
        self.getSummary()[self.get_class_key()]['status' ] ="processed"
        self.getLogger().log('Run')

def main():
    import os
    from dotenv import load_dotenv
    from util import Util
    load_dotenv()
    dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'

    load = ProcessLoadDataworldPatch20190927(dw_source).run()

    assert load.get_class_key() == '01.ProcessLoadDataworldPatch20190927'
    #assert load.get_history_folder().endswith('history')

if __name__ == "__main__":
    main()