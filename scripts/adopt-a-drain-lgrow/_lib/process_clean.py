from process import Process

class ProcessClean(Process):
    def __init__(self, df_source, commonNameMap, region_map, jurisdiction_map):
        Process.__init__(self)
        self.dataframe = df_source
        self.commonNameMap = commonNameMap
        self.region_map=region_map
        print('dr_jurisdiction D')
        self.jurisdiction_map=jurisdiction_map