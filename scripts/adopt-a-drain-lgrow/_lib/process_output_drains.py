from process_outputs import ProcessOutputs
from config_output_columns import ConfigOutputColumns
from helper import Helper

class ProcessOutputDrains(ProcessOutputs):
    def __init__(self, wrangle,output_file_name, expected_output_columns_list=ConfigOutputColumns()):
        ProcessOutputs.__init__(self, wrangle.get_dataframe(), expected_output_columns_list)
        self.summary_key ='05'
        self.output_file_name = output_file_name

        #self.output_file_name = '{}/{}'.format(Helper().get_clean_data_folder(), output_file_name)


    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def validateOutputColumns(self):
        # examine for extra cols not needed for data.world
        for nm in self.get_dataframe().columns.values:
            if not nm in self.expected_output_columns_list:
                raise Exception('{} is unexpected output for clean data'.format(nm))


    def toCSV(self):
        output_name = '{}/{}'.format(Helper().get_clean_data_folder(), self.output_file_name)

        self.get_dataframe().to_csv(output_name, index=False)
        #self.get_dataframe().to_csv(local_config["local_clean"], index=False)
        return self

    def process(self):
        helper = Helper()
        print('* ProcessOutputs')
        self.validateOutputColumns()
        print('output: ', self.output_file_name)

        self.toCSV() # write data to disk

        # print(' - output folder: ','data.world/clean-data/adopt-a-drain/')
        #print(' - output file: ' ,'/data.world/clean-data/adopt-a-drain/', metadata['output_file_name'] )
        #print(' - data.world file: ' ,'/data.world/clean-data/adopt-a-drain/', metadata['copy_file_name'] )

        for colname in self.get_dataframe().columns.values:
            print(' -- column: ', colname )

        # OUTPUT_FILE_NAME
        '''
        ifn = '{}/{}'.format(helper.get_clean_data_folder(), metadata['output_file_name'])
        ofn = '{}/{}'.format(helper.get_clean_data_folder(), metadata['copy_file_name'])

        copyfile(ifn, ofn)
        # set up a smaller version of file
        tfn = '{}/{}'.format(helper.get_test_version_folder(), metadata['copy_file_name'])
        # df_small = df_source.query("dr_jurisdiction = 'City of Grand Rapids'")
        print(' - make short file for testing: ', '/data.world/test-data/adopt-a-drain/', metadata['copy_file_name'])
        df_small =self.get_dataframe().query("dr_jurisdiction == 'City of Grand Rapids'").head(5000)
        df_small.to_csv( tfn, index=False)
        '''

def main():
    from helper import Helper
    from process_load_dataworld_patch_20190927 import ProcessLoadDataworldPatch20190927
    from process_wrangle import ProcessWrangle
    from util import Util

    #output_folder = '{}/myfilename.csv'.format(Helper().get_clean_data_folder())
    #print('output folder: ', Helper().get_clean_data_folder())

    dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'
    loadDataWorld = ProcessLoadDataworldPatch20190927(dw_source).run()
    wrangle = ProcessWrangle(loadDataWorld).run()
    output = ProcessOutputDrains(wrangle,'current.csv').run()
    print('{}/{}'.format(Helper().get_clean_data_folder(),'current.csv'))
    Util().deleteFile(Helper().get_clean_data_folder(),'current.csv')


if __name__ == "__main__":
    main()
