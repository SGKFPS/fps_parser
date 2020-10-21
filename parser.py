import glob
import os
import pandas as pd


def createDf():

    folder_list = glob.glob('./RawData/*')

    print(folder_list)

    for fl in folder_list:
        files = glob.glob(fl+"/*.xlsx")

        df = pd.DataFrame()
        for f in files:
            data = pd.read_excel(f)
            print(data.loc[[0]])
            #print(data)
            #df.append(data)
        



