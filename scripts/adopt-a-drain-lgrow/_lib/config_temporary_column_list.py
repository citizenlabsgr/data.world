class ConfigTemporaryColumnList(list):
    # list of column that need to be removed before saving
    # aka extraColumns
    def __init__(self):
        self.extend(['del_source',
              'del_fid',
              'del_gid',
              'source_code',
              'dr_local_id',
              'dr_facility_id',
              'dr_location',
              'dup_coordinate'])

def main():
    print('finish me')
    lst = ConfigTemporaryColumnList()
    print('lst: ', lst)

if __name__ == "__main__":
    main()