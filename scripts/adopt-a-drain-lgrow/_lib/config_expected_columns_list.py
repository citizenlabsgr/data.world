class ConfigExpectedColumnsList(list):
    # list of columns that are expected in the file header
    # aka expected_process_columns_list
    def __init__(self):
        self.extend(['facility_prefix',
                         'dr_subtype',
                         'dr_jurisdiction',
                         'dr_owner',
                         'dr_subwatershed',
                         'dr_lon',
                         'dr_lat',
                         'dr_asset_id',
                         'dr_type',
                         'dr_sync_id',
                         'dr_discharge'])



def main():
    print('finish me')
    lst = ConfigExpectedColumnsList()
    print('lst: ', lst)

if __name__ == "__main__":
    main()
