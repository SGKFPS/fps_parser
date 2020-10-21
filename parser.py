import glob
import os
import pandas as pd


def createDf():

    folder_list = glob.glob('./RawData/*')

    print(folder_list)

    for fl in folder_list:
        files = glob.glob(fl+"/*.xlsx")

        dfs = []
        #df = pd.DataFrame()
        for f in files:
            name = f[:-5]
            name = name.split("_", 1)[1]
            #print(name)

            data = pd.read_excel(f, header=5)
            data = data[5:400]
            data = data.reset_index(drop=True)

            data =  data.dropna(1, how='all')
            del data['Asset status']

            #print(data.columns)
            data.columns = data.columns.map(lambda x : name+"_"+x if x =='Actual (kWh)' or x == 'Baseline (kWh)' else x)
            #data = data.add_prefix(name)
            #df.append(data)
            data = data.set_index('Date')
            #print(data)
            dfs.append(data)
            print(data)
            #df.append(data)
        #print(dfs)


        df = dfs[0]

        for fs in dfs[1:]:
            df = df.join(fs, how='outer')
            #df = df.drop_duplicates()
            #print(df)

        output = fl.split("/")[2]
        df.to_csv(output+".csv")
        print("heyyyyy")
