from process import Process
import numpy as np

class ProcessCondense(Process):
    def __init__(self, dataframe, expected_output_columns_list, extraColumns, outlier_settings):
        Process.__init__(self)
        self.dataframe = dataframe
        self.expected_output_columns_list = expected_output_columns_list
        self.extraColumns = extraColumns
        self.outlier_settings = outlier_settings
        self.summary_key = '06'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def validateColumns(self):
        print(' - validate columns')
        '''
        check column name for the expected colnames
        '''
        for nm in self.expected_output_columns_list:
            if not nm in self.get_dataframe().columns.values:
                raise Exception('{} is missing from '.format(nm))

    def removeExtraColumns(self):
        print(' - Remove extra columns')
        for colname in self.extraColumns:
            if (colname in self.get_dataframe().columns.values):
                print(' -- drop column: ', colname)
                self.set_dataframe(self.get_dataframe().drop([colname], axis=1))

    def remove_obvious_outliers(self):
        print(' - remove outliers')
        '''
        remove individual observations
        remove range of observation

        '''
        #         for outlier in self.outlier_settings['outliers']:

        for outlier in self.outlier_settings:
            #pprint(outlier)
            col_name = outlier['column']

            if 'range' in outlier:

                low = outlier['range'][0]
                high = outlier['range'][1]
                sz = len(self.get_dataframe())

                tmp = None
                tmp1 = ''

                if isinstance(low, np.datetime64):
                    self.set_dataframe(
                        self.get_dataframe()[(self.get_dataframe()[col_name].to_datetime() >= low) & (
                                    self.get_dataframe()[col_name].to_datetime() <= high)]
                    )
                else:
                    self.set_dataframe(
                        #print('col_name', col_name)
                        self.get_dataframe()[
                            (self.get_dataframe()[col_name] >= low) & (self.get_dataframe()[col_name] <= high)]
                    )
                outlier["count"] = sz - len(self.get_dataframe())

            elif 'categories' in outlier:
                _list = outlier['categories']
                sz = len(self.get_dataframe())
                self.set_dataframe(
                    self.get_dataframe()[self.get_dataframe()[col_name].isin(_list)]
                )
                outlier["count"] = sz - len(self.get_dataframe())
            if "reason" in outlier:
                outlier["reason"] = outlier["reason"].format(str(outlier["count"]))

    def remove_duplicate_assets(self):
        print(' - drop duplicate assets')
        key = 'dr_asset_id'
        sz1 = len(self.get_dataframe())

        self.set_dataframe(self.get_dataframe().drop_duplicates(key, keep='first'))
        sz2 = len(self.get_dataframe())

        if 'duplicates' not in self.getSummary()[self.get_class_key()]:
            self.getSummary()[self.get_class_key()]['duplicates'] = []

        self.getSummary()[self.get_class_key()]['duplicates'].append(
            {'dr_asset_id': {'before': sz1, 'after': sz2, 'diff': (sz2 - sz1)}})

    def remove_duplicate_coordinates(self):
        print(' - drop duplicate coordinates')
        print(' - cols ', self.get_dataframe().columns.values)

        # print(' -- add coordinate')
        # self.get_dataframe()['dup_coordinate'] = '(' + self.dataframe['dr_lon'].astype(str) + ' ' + self.dataframe['dr_lat'].astype(str) + ')'

        sz1 = len(self.get_dataframe())

        self.set_dataframe(self.get_dataframe().sort_values('dup_coordinate'))
        self.set_dataframe(self.get_dataframe().drop_duplicates('dup_coordinate', keep='first'))

        sz2 = len(self.get_dataframe())

        if 'duplicates' not in self.getSummary()[self.get_class_key()]:
            self.getSummary()[self.get_class_key()]['duplicates'] = []

        self.getSummary()[self.get_class_key()]['duplicates'].append(
            {'coordinates': {'before': sz1, 'after': sz2, 'diff': (sz2 - sz1)}})

        # self.summary['duplicates'].append({'coordinates': {'before':sz1, 'after':sz2, 'diff':(sz1-sz2)}})
        # self.summary['duplicates'].append({'coordinates':(sz1-sz2)})

    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe

    def process(self):
        print('* ProcessCondense')
        self.getSummary()[self.get_class_key()] = {}
        self.getSummary()[self.get_class_key()]['before'] = len(self.get_dataframe())
        self.remove_duplicate_assets()
        # self.remove_duplicate_coordinates()
        self.remove_obvious_outliers()

        self.removeExtraColumns()

        self.validateColumns()
        self.getSummary()[self.get_class_key()]['after'] = len(self.get_dataframe())
        diff = (self.getSummary()[self.get_class_key()]['before'] - self.getSummary()[self.get_class_key()]['after'])
        self.getSummary()[self.get_class_key()]['diff'] = diff

def main():
    print('finish me')

if __name__ == "__main__":
    main()