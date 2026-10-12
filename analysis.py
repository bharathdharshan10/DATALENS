import pandas as pd



def get_statistics(data):
    return data.describe()


def get_head(data):
    return data.head()

def get_isnull(data):
    return data.isnull().sum()

def get_rows(data):
    return data.shape[0]

def get_duplicate(data):
    return data.duplicated().sum()




