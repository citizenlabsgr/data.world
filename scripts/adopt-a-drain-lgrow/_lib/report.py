class Report(dict):
    def __init__(self):
        self.report_file_name = 'report.json'

    def stepReport(self, nameKey, df):
        self[nameKey]={}
        self[nameKey]['rows']=len(df.index)
        self[nameKey]['cols']=len(df.columns)
        return self

def main():
    from process_load_dataworld_patch_20190927 import ProcessLoadDataworldPatch20190927

    import os
    from dotenv import load_dotenv
    from util import Util
    load_dotenv()
    # dw_source = 'citizenlabs/grb-storm-drains-2019-04-03'
    dw_source = 'citizenlabs/lgrow-storm-drains-current'

    load = ProcessLoadDataworldPatch20190927(dw_source).run()
    rpt = Report()

    rpt.stepReport('step-one',load.get_dataframe())
    rpt.stepReport('step-two',load.get_dataframe())

    print('report ', rpt)

if __name__ == "__main__":
    main()

