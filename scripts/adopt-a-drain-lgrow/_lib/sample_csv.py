from process import Process
import pandas as pd
import csv
import os
from util import Util

class SampleCSV(list):
    def __init__(self, filename='_raw_.csv'):
        self.filename = filename
        self.append(["FID", "StrType", "JURISDICTI", "OWNER", "Source", "LOCAL_ID", "FACILITYID", "Lat", "Long", "Subbasin"])
        self.append([0, 15, "Village of Caledonia", "Village of Caledonia", "Village of Caledonia", "", "C252", 42.7427204491, -85.4147974205, "Lower Thornapple River"])
        self.append([1, 15, "Village of Caledonia", "Village of Caledonia", "Village of Caledonia", "", "C253", 42.7427204491, -85.4147974205, "Lower Thornapple River"])
        self.append([2, 15, "Village of Caledonia", "Village of Caledonia", "Village of Caledonia", "", "C268", 42.7427204491, -85.4147974205, "Lower Thornapple River"])

        #self.append(['FID', 'SubType', 'JURISDICTI',            'OWNER',               'Source',              'LOCAL_ID','FACILITYID','Lat',         'Long',        'Subbasin'])
        #self.append([ 0,     15,       'A Village of Caledonia','Village of Caledonia','Village of Caledonia','','C252',         42.7427204491,-85.4147974205,'Lower Thornapple River'])
        #self.append([1,15,'B Village of Caledonia','Village of Caledonia','Village of Caledonia','','C253',42.742,-85.41, 'Lower Thornapple River'])
        # duplicate row
        #self.append([1,15,'C Village of Caledonia','Village of Caledonia','Village of Caledonia','','C254',42.742,-85.41, 'Lower Thornapple River'])

    def getFileName(self):
        return self.filename

    def getDF(self):
        return pd.read_csv(self.filename)

    def delete(self):
        Util().deleteFile(os.getcwd(), self.filename)
        return self

    def write(self):
        with open(self.filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the data rows
            csvwriter.writerows(self)
        return self




class dep_SampleCSV(Process):
    def __init__(self, filename='_raw_.csv'):
        # no folder, just create it wherever
        self.filename=filename
        self.fields = ["FID", "SubType", "JURISDICTI", "OWNER","Source","LOCAL_ID","FACILITYID","Lat","Long","Subbasin"]

    def getClassName(self):
        return self.__class__.__name__

    def getFilename(self):
        return self.filename

    def getSampleData(self):
        return [[0,15,'Village of Caledonia','Village of Caledonia','Village of Caledonia','C252',42.7427204491,- 85.4147974205,'Lower Thornapple River'],
         [1,15,'Village of Caledonia','Village of Caledonia','Village of Caledonia','C253',42.7427204491, - 85.4147974205, 'Lower Thornapple River']]

    def getDF(self):
        return pd.read_csv(self.filename)

    def delete(self):
        Util().deleteFile(os.getcwd(), self.filename)
        return self

    def process(self):
        #raise Exception('Overload process() in {}'.format(self.getClassName()))
        # writing to csv file
        with open(self.filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(self.fields)

            # writing the data rows
            csvwriter.writerows(self.getSampleData())

    def run(self):
        self.process()
        return self

def main():

    _file = SampleCSV().write()

    print(_file.getDF().dtypes)

    assert Util().file_exists('.',_file.getFileName())
    assert _file.getFileName() == '_raw_.csv'

    #_file.delete()
    assert not Util().file_exists('.',_file.getFileName())


if __name__ == "__main__":
    main()