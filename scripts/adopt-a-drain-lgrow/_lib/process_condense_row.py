from process_condense import ProcessCondense
from config_output_columns import ConfigOutputColumns
from config_temporary_column_list import ConfigTemporaryColumnList
from config_outlier_settings import ConfigOutlierSettings
import pprint

class ProcessCondenseRows(ProcessCondense):
    def __init__(self, clean, expected_output_columns_list=ConfigOutputColumns(), extraColumns=ConfigTemporaryColumnList(), outlier_settings=ConfigOutlierSettings()):
        ProcessCondense.__init__(self, clean.get_dataframe(), expected_output_columns_list, extraColumns, outlier_settings)
        self.summary_key ='04'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def process(self):
        print('* RowCondense')
        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['before' ] =len(self.get_dataframe())

        self.remove_duplicate_assets()
        self.remove_duplicate_coordinates()
        self.remove_obvious_outliers()

        self.getSummary()[self.get_class_key()]['after' ] =len(self.get_dataframe())

        diff =(self.getSummary()[self.get_class_key()]['after' ] -self.getSummary()[self.get_class_key()]['before'])
        self.getSummary()[self.get_class_key()]['diff'] = diff

def main():

    from sample_csv import SampleCSV
    from process_load_drains import ProcessLoadDrains
    from config_common_name_map import ConfigCommonNameMap
    from config_region_map import ConfigRegionMap
    from process_clean_drains import ProcessCleanDrains
    from config_output_columns import ConfigOutputColumns
    from config_temporary_column_list import ConfigTemporaryColumnList
    from config_outlier_settings import ConfigOutlierSettings
    from util import Util

    # create a file
    sampleCSV = SampleCSV().write()
    print(sampleCSV.getDF())
    # ProcessLoad
    load = ProcessLoadDrains(sampleCSV.getFileName()).run()
    print('row count: ', len(load.get_dataframe()))

    assert len(load.get_dataframe()) == 3
    # ProcessClean
    clean = ProcessCleanDrains(load ).run()

    # ProcessCondense Rows
    condense = ProcessCondenseRows(clean).run()

    assert condense.get_class_key() == '04.ProcessCondenseRows'
    #print(condense_rows.get_dataframe())

    print('row count: ', len(condense.get_dataframe()))
    assert len(condense.get_dataframe()) < 3

    pprint.pprint(condense.getSummary())
    print(condense.get_dataframe())
    # clean up
    sampleCSV.delete()


if __name__ == "__main__":
    main()