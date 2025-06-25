import pandas as pd


class Data:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.columns = self.df.columns