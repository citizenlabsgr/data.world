

class ConfigOutputColumns(list):
    # expected output columns
    # aka expected_output_columns_list
    def __init__(self):
        self.extend(['dr_asset_id',
                              'dr_jurisdiction',
                              'dr_lat',
                              'dr_lon',
                              'dr_owner',
                              'dr_subtype',
                              'dr_subwatershed',
                              'dr_type',
                              'dr_discharge'
                             ])

def main():
    output_colunns = ConfigOutputColumns()
    assert output_colunns[0]=='dr_asset_id'
    print(output_colunns)

if __name__ == "__main__":
    main()
