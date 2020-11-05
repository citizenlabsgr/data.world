import os
import os.path
from helper import Helper

class ProcessLogger:
    '''
    collects the process steps along the way
    then prints them
    '''
    def __init__(self,log_file_name='process.log',log_file_folder=Helper().get_history_folder()):
        self.file_name = log_file_name
        self.file_folder = log_file_folder
        self.markdown_list = []

    '''
    def __init__(self,log_file_name=None):

        if log_file_name != None:
            self.file_name = log_file_name
        else:
            self.file_name = 'process.log'
        self.markdown_list = []
    '''

    def get_file_name(self):
        return '{}/{}'.format(self.file_folder,self.file_name)

    def kill(self):

        if os.path.isfile(self.get_file_name()):
            print('kill log: ',self.get_file_name())
            os.remove(self.get_file_name())
        else:
            print('no kill: ', self.get_file_name())
        return self

    def log(self, stringValue):
        print('processlogger: ', self.get_file_name())
        with open(self.get_file_name(), "a") as myfile:
            myfile.write(stringValue+'\n')
        return self

    def collect(self,markup):
        self.markdown_list.append(markup)
        return self

    def getMarkdown(self):
        return '\n'.join(self.markdown_list)

    def clear(self):
        self.markdown_list = []
        return self
    def show(self):
        print( self.markdown_list )

def main():
    pl = ProcessLogger()
    pl.kill()
    pl.log("HI")
    pl.log("Ho")


if __name__ == "__main__":
    # execute only if run as a script
    main()