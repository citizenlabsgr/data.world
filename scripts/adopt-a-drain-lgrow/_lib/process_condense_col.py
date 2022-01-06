from process_condense import ProcessCondense
from config_output_columns import ConfigOutputColumns
from config_temporary_column_list import ConfigTemporaryColumnList
from config_outlier_settings import ConfigOutlierSettings

class ProcessCondenseColumns(ProcessCondense):
    def __init__(self, condense_row, expected_output_columns_list=ConfigOutputColumns(), extraColumns=ConfigTemporaryColumnList(), outlier_settings=ConfigOutlierSettings()):
        ProcessCondense.__init__(self, condense_row.get_dataframe(), expected_output_columns_list, extraColumns, outlier_settings)
        #self.summary_key ='04'
        self.setSummaryNo('04')

    #def get_class_key(self):
    #    return '{}.{}'.format(self.summary_key, self.getClassName())

    def process(self):
        #print('* ColCondense')
        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['from' ] =[c for c in self.get_dataframe().columns]

        self.removeExtraColumns()

        self.validateColumns()
        self.getSummary()[self.get_class_key()]['to' ] =[c for c in self.get_dataframe().columns]
        # diff=(self.getSummary()[self.get_class_key()]['before']-self.getSummary()[self.get_class_key()]['after'])
        # self.getSummary()[self.get_class_key()]['diff'] = diff

def main():
    #from sample_csv import SampleCSV
    #from output_columns import OutputColumns
    #from outlier_settings import OutlierSettings
    #from list_columns_temporary import ListColumnsTemporary
    #from map_regions import MapRegions

    #df = SampleCSV().run().getDF()

    #condense = ProcessCondenseColumns(df, OutputColumns(), ListColumnsTemporary(), OutlierSettings()).run()
    #SampleCSV().delete()


    from sample_csv import SampleCSV
    from process_load_drains import ProcessLoadDrains
    from process_clean_drains import ProcessCleanDrains
    from process_condense_row import ProcessCondenseRows
    from util import Util

    # create a file
    sampleCSV = SampleCSV().write()

    # ProcessLoad
    load = ProcessLoadDrains(sampleCSV.getFileName()).run()

    # ProcessClean
    clean = ProcessCleanDrains(load ).run()

    # ProcessCondense Rows
    condense_row = ProcessCondenseRows(clean).run()

    # Condense Columns
    condense_c = ProcessCondenseColumns(condense_row).run()

    assert condense_c.get_class_key() == '05.ProcessCondenseColumns'

    # clean up
    sampleCSV.delete()

if __name__ == "__main__":
    main()