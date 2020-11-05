from process import Process
from process_clean import ProcessClean
from config_common_name_map import ConfigCommonNameMap
from config_region_map import ConfigRegionMap
import numpy as np

class ProcessCleanDrains(ProcessClean):
    def __init__(self, load, commonNameMap=ConfigCommonNameMap(), region_map=ConfigRegionMap()):
        ProcessClean.__init__(self ,load.get_dataframe(), commonNameMap, region_map)

        self.summary_key ='03'

    def get_class_key(self):
        return '{}.{}'.format(self.summary_key, self.getClassName())

    def clean_column_names(self):
        '''
        convert each column to lowercase with underscore seperation

        e.g., ID to id
        e.g., County ID to county_id
        e.g., County-ID to county_id
        :param actual_col_list: list of column names
        :return: clean list of column names

        {
          'field-name': {}
        }

        '''
        # start_time = time.time()

        actual_col_list = self.dataframe.columns
        clean_column_names = {}
        for cn in actual_col_list:

            ncn = cn
            # get rid of some unwanted characters

            if ' ' in cn:
                ncn = cn.replace(' ' ,'_')

            if '-' in cn:
                ncn = cn.replace('-', '_')

            # force first char to lower case
            nncn = ncn
            ncn = ''
            prev_upper = True  # False
            case = False
            camelcase = False
            for c in nncn:
                if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    case = True
                    if prev_upper:
                        ncn += c.lower()
                    else:
                        ncn += '_' + c.lower()
                        camelcase = True
                    prev_upper = True
                else:
                    ncn += c
                    prev_upper = False

            clean_column_names[cn] =ncn

        return self.dataframe.rename(columns=clean_column_names)
        # print('* clean_column_names: {} sec'.format(time.time() - start_time))  # time_taken is in seconds


    def inferName(self, col_name):
        '''
        select a column name based on previous names found in file
        '''
        '''
        names = {
            
            "subtype": "dr_subtype",
            "jurisdicti": "dr_jurisdiction",
            "drain__owner": "dr_owner",
            "owner" :"dr_owner",
            "local__id": "dr_local_id",
            "facilityid": "dr_facility_id",
            "drain__jurisdiction": "dr_jurisdiction",
            "subwatershed": "dr_subwatershed",
            "subbasin": "dr_subwatershed",
            "point__x" :"dr_lon",
            "long": "dr_lon",
            "point__y" :"dr_lat",
            "lat" :"dr_lat",
            "soure__id": "del_source_id"}
        '''
        #names = ConfigCommonNameMap()
        if not col_name in self.commonNameMap:
            # mark madeup names for easy id later
            print('unexpected ', col_name)
            return 'del_{}'.format(col_name)

        return self.commonNameMap[col_name]

    def getColumnDict(self):

        col_dict = {}
        for nm in self.dataframe.columns.values:
            col_dict[nm] =self.inferName(nm)
        return col_dict

    def remove_char(self ,columnList):
        '''
        some facillity ids have characters mixed wtih number
        we need just the number part
        this function removes all characters from the facility id
        '''
        newList = []

        for item in columnList:
            fi = ''
            for ch in str(item):
                if ch in '0123456789':
                    fi += ch
                else:
                    fi += '0'
            newList.append(fi)

        return newList

    def regional_codes(self, df_source , _owner):
        '''
        regional codes identify the data's source community
        code are added over time. this method checks and throws error not found.
        fix by adding new owner and code to list below
        '''
        # print('regional_code 1')
        rc = []

        # look at data in in the _owner column
        for jur in self.dataframe[_owner]:
            # check if jur is in the codes
            jur = jur.strip()
            if jur in self.region_map:
                rc.append(self.region_map[jur])
            else:
                print('bad name', )
                raise Exception('Regional-Code for ({}) is not available... manually add new to ConfigRegionMap'.format(jur))
                # rc.append('XXX')

        return rc

    def get_dataframe(self):
        return self.dataframe

    def process(self):
        self.getSummary()[self.get_class_key() ] ={}
        self.getSummary()[self.get_class_key()]['before' ] =len(self.get_dataframe())
        '''
        clean up the df_source
        '''
        self.dataframe = self.clean_column_names()
        self.dataframe = self.dataframe.rename(columns=self.getColumnDict())

        # create col to compare duplicate coordinates
        print(' -- add coordinate')
        self.dataframe['dup_coordinate'] = '(' + self.dataframe['dr_lon'].astype(str) + ' ' + self.dataframe['dr_lat'].astype(str) + ')'

        # print('dup_coordinate',self.dataframe['dup_coordinate'])
        # patch up bad owner and jurisdiction names
        # print(' -- replace dr_jurisdiction with dr_owner')
        self.dataframe['dr_jurisdiction'] = self.dataframe['dr_owner'] # is what it is

        # mark all empties with nan
        print(' -- identify empty dr_facility_ids')
        self.dataframe['dr_facility_id'] = self.dataframe['dr_facility_id'].apply \
            (lambda x:  np.nan if x != x or x == '' or x == ' ' or x == None else x)

        # some dr_facilities have alfa numeric values ... clean up
        print(' -- remove char from dr_facility_id')
        self.dataframe['dr_facility_id'] = self.remove_char(self.dataframe['dr_facility_id'])

        # add colunm to id the source of data records
        print(' -- create field: source_code from dr_owner')
        self.dataframe['source_code'] = self.regional_codes( self.dataframe , 'dr_owner')

        # convert typ to integer
        print(' -- int-ify field: dr_facility_id')
        self.dataframe['dr_facility_id'] = self.dataframe['dr_facility_id'].astype('int64')

        # create final id aka dr_asset_id
        print(' -- create field: dr_asset_id from source_code, dr_facility_id')
        self.dataframe['dr_asset_id'] = self.dataframe['source_code'] + '_' + self.dataframe['dr_facility_id'].astype \
            (str)

        print(' -- create field: dr_type from constant "Storm Water Inlet Drain"')
        self.dataframe['dr_type'] = self.dataframe['dr_asset_id'].apply(lambda x: 'Storm Water Inlet Drain')

        # add dr_discharge column
        print(' -- create field: dr_discharge from dr_subwatershed')
        self.dataframe['dr_discharge'] = self.dataframe['dr_subwatershed']

        self.getSummary()[self.get_class_key()]['after' ] =len(self.get_dataframe())
        diff = self.getSummary()[self.get_class_key()]['after']  - self.getSummary()[self.get_class_key()]['before']
        self.getSummary()[self.get_class_key()]['diff'] = diff


def main():
    from sample_csv import SampleCSV
    from process_load_drains import ProcessLoadDrains
    from config_common_name_map import ConfigCommonNameMap
    from config_region_map import ConfigRegionMap

    from util import Util

    # create a file
    sampleCSV = SampleCSV().write()

    # ProcessLoad
    load = ProcessLoadDrains(sampleCSV.getFileName()).run()
    #print(list(load.get_dataframe().columns))

    # ProcessClean
    #clean = ProcessCleanDrains(load, ConfigCommonNameMap(), ConfigRegionMap()).run()
    clean = ProcessCleanDrains(load).run()

    assert clean.get_class_key() == '03.ProcessCleanDrains'
    #print('out ',list(clean.get_dataframe().columns))
    #                                             ['del_fid', 'del_sub_type', 'dr_jurisdiction', 'dr_owner', 'del_source', 'dr_local_id', 'dr_facility_id', 'dr_lat', 'dr_lon', 'dr_subwatershed', 'dup_coordinate', 'source_code', 'dr_asset_id', 'dr_type', 'dr_discharge']
    #                                        out  ['del_fid', 'dr_sub_type', 'dr_jurisdiction', 'dr_owner', 'del_source', 'dr_local_id', 'dr_facility_id', 'dr_lat', 'dr_lon', 'dr_subwatershed', 'dup_coordinate', 'source_code', 'dr_asset_id', 'dr_type', 'dr_discharge']
    print(list(clean.get_dataframe().columns))
    assert list(clean.get_dataframe().columns) == ['del_fid', 'dr_subtype', 'dr_jurisdiction', 'dr_owner', 'del_source', 'dr_local_id', 'dr_facility_id', 'dr_lat', 'dr_lon', 'dr_subwatershed', 'dup_coordinate', 'source_code', 'dr_asset_id', 'dr_type', 'dr_discharge']
    #print(clean.get_dataframe().dftypes())
    # clean up
    sampleCSV.delete()

if __name__ == "__main__":
    main()