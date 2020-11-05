from process import Process

class ProcessOutputs(Process):
    def __init__(self, df_source, expected_output_columns_list):
        Process.__init__(self)
        self.dataframe = df_source
        self.expected_output_columns_list = expected_output_columns_list
