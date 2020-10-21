import glob
import os
import pandas as pd


def createDf():

    folder_list = glob.glob('./RawData/*')

    print(folder_list)

    for fl in folder_list:
        files = glob.glob(fl+"/*.xlsx")

        dfs = []
        for f in files:
            name = f[:-5]
            name = name.split("_", 1)[1]

            data = pd.read_excel(f, header=5)
            data = data[5:]
            data = data.reset_index(drop=True)

            data =  data.dropna(1, how='all')
            del data['Asset status']

            
            data.columns = data.columns.map(lambda x : name+"_"+x if x =='Actual (kWh)' or x == 'Baseline (kWh)' else x)
            data = data.set_index('Date')
            dfs.append(data)



        df = dfs[0]

        for fs in dfs[1:]:
            df = df.merge(fs, how='outer', left_index=True, right_index=True)
            df = df[~df.index.duplicated(keep='first')]

            #print(df)

        output = fl.split("/")[2]
        df.to_csv(output+".csv")
        print("Done with "+output)
