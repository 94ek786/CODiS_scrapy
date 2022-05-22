import pandas as pd
import copy


train = [[2020, 1], [2022, 1]]
test = [[2022, 1], [2022,6]]
M_T = ['00','01','02','03','04','05','06','07','08','09','10','11','12']

def data(time_range):
    df = pd.DataFrame()
    loop = copy.deepcopy(time_range[0])
    while(loop != time_range[1]):
        df1 = pd.read_csv('south_station/C0R570-' + str(loop[0]) + '-' + M_T[loop[1]] + '.csv')
        df1.columns = df1.iloc[0]
        df1 = df1.drop(df1.index[0])
        #print(df1.head(2))
        df_d = df1[['ObsTime','Temperature']]
        df_d = df_d.reset_index(drop=True)
        #print(df_d.head(2))
        for loop1 in range(df_d.shape[0]):
            df_d.iloc[loop1, 0] = str(loop[0]) + '/' + M_T[loop[1]] + '/' + df_d.iloc[loop1, 0]
        #print(df_d.head(2))

        df = pd.concat([df, df_d])
        if(loop[1] == 12):
            loop[0] += 1
            loop[1] = 1
        else:
            loop[1] += 1

    df = df.reset_index(drop=True)
    df = df.drop(df[df['Temperature'] == '...'].index)
    return df

data(train).to_csv('train.csv', index=False)
data(test).to_csv('test.csv', index=False)