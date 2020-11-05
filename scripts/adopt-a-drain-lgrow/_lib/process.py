
from util_processlogger import ProcessLogger
from helper import Helper
import os

class Process():
    def __init__(self):
        self.summary = {}  # stash process results, counts, here
        #self.logger = Process Logger('./{}/{}.ran'.format(self.get_history_folder(), self.getClassName()))
        self.logger = None
        #self.logger = Process Logger('./history/{}.ran'.format(self.getClassName()))

    def getClassName(self):
        return self.__class__.__name__

    def getLogger(self):
        if self.logger is None:
            #self.logger = ProcessLogger('{}/{}.ran'.format(Helper().get_history_folder(), self.getClassName()))
            self.logger = ProcessLogger(log_file_name='{}.ran'.format(self.getClassName()))
        return self.logger
    '''
    def get_history_folder(self):
        
        #returns path to the repo folder from script path
        
        scripts_path = os.getcwd()
        rc = ''
        rc = scripts_path \
            .replace('/scripts', '') \
            .replace('/' + '_lib', '')
        rc = '{}/data/_history'.format(rc)
        return rc
    '''
    def getSummary(self):
        return self.summary

    def setSummary(self, summary):
        self.summary = summary
        return self

    def filename(self, in_f):
        ps = in_f.split('/')
        return ps[len(ps) - 1]

    def process(self):
        raise Exception('Overload process() in {}'.format(self.getClassName()))

    def run(self):
        self.process()
        return self

def main():
    process = Process()

    assert process.getSummary() == {}
    assert process.filename('/a/b/c/some.csv')
    #print('history_folder: ' + process.get_history_folder())
    #assert process.get_history_folder().endswith('data/_history')


if __name__ == "__main__":
    main()