import pandas as pd

class ConfigJurisdictionMap(dict):
    def __init__(self):
        self.update({
        "Kent County Road Commission": "Kent County Road Commission",
        "KENT COUNTY ROAD COMMISSION":"Kent County Road Commission",
        "City of East Grand Rapids": "City of East Grand Rapids",
        "City of Grandville": "City of Grandville",
        "City of Wyoming": "City of Wyoming",
        "City of Kentwood": "City of Kentwood",
        "Grand Rapids Township": "Grand Rapids Township",
        "City of Walker": "City of Walker",
        "CGR": "City of Grand Rapids",
        "City of Grand Rapids": "City of Grand Rapids",
        "Georgetown Township": "Georgetown Township",
        "City of Hudsonville": "City of Hudsonville",
        "Jamestown Township": "Jamestown Township",
        "Cascade Township": "Cascade Township",
        "Algoma Township": "Algoma Township",
        "Grattan Township": "Grattan Township",
        "Gaines Township": "Gaines Township",
        "Vergennes Township": "Vergennes Township",
        "Lowell Township": "Lowell Township",
        "Oakfield Township": "Oakfield Township",
        "Cannon Township": "Cannon Township",
        "Sparta Township": "Sparta Township",
        "Solon Township": "Solon Township",
        "Ada Township": "Ada Township",
        "City of Lowell": "City of Lowell",
        "Bowne Township": "Bowne Township",
        "Tyrone Township": "Tyrone Township",
        "Caledonia Township": "Caledonia Township",
        "Courtland Township": "Courtland Township",
        "Spencer Township": "Spencer Township",
        "Village of Sparta": "Village of Sparta",
        "BYRON TOWNSHIP": "Byron Township",
        "CALEDONIA TOWNSHIP": "Calidonia Township",
        "City of Rockford": "City of Rockford",
        "Alpine Township": "Alpine Township",
        "Plainfield Township": "Plainfield Township",
        "Byron Township": "Byron Township",
        "Village of Spring Lake": "Village of Spring Lake",
        "Village of Spring Lake DPW": "Village of Spring Lake",
        "OCWRC": "Ottawa County Water Resource Commissioner",
        "Ottawa County Road Commission": "Ottawa County Water Resource Commissioner",
        "OCRC": "Ottawa County Water Resource Commissioner",
        "Ottawa County Water Resource Commissioner":"Ottawa County Water Resource Commissioner",
        "Village of Fruitport":"Village of Fruitport",
        "Village of Caledonia":"Village of Caledonia",
        "City of Grand Haven DPW": "City of Grand Haven DPW",
        "OC Facilities":"Ottawa County Facilities"
    })

    def columnValues(self, df_source, _owner='dr_owner'):
        '''
        Fix misnamed jurisdiction names
        '''
        print('size ', len(df_source['dr_owner']))
        rc = []
        #print(df_source.columns)
        # look at data in in the _owner column
        for jur in df_source[_owner]:
            # check if jur is in the codes
            jur = jur.strip()
            if jur in self:
                rc.append(self[jur])
            else:
                print('bad name', )
                raise Exception(
                    'Jurisdiction for ({}) is not available... manually add new to ConfigJurisdictionMap'.format(jur))

        return rc

def main():
    # from process_load_dataworld_patch_20190927 import ProcessLoadDataworldPatch20190927
    map = ConfigJurisdictionMap()

    data = {

        "dr_owner": ['OCWRC',
                     'Kent County Road Commission',
                     'KENT COUNTY ROAD COMMISSION',
                     'OC Facilities'],
        "dr_jurisdiction": ['aaa',
                     'Kent',
                     'KENT',
                     'OC']
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(data)

    assert map['Kent County Road Commission'] == 'Kent County Road Commission'
    assert map['KENT COUNTY ROAD COMMISSION'] == 'Kent County Road Commission'

    print(df)

    df['dr_jurisdiction'] = map.columnValues(df)

    print(df)

    #dw_source = 'citizenlabs/lgrow-storm-drains-current'
    #loadDataWorld = ProcessLoadDataworldPatch20190927(dw_source).run()
    # wrangle = ProcessWrangle(loadDataWorld).run()
    # dw_source = 'citizenlabs/lgrow-storm-drains-current'

if __name__ == "__main__":
    main()