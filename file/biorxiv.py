import pandas as pd
import glob

folderlist = glob.glob('../outputcsv/*')

df_list = []
for folder in folderlist:
    try:
        df_list.append(pd.read_csv(folder+'/biorxiv.csv', delimiter='\t'))
    except:
        pass
print(len(df_list))

df_all = pd.concat(df_list)
df_all.drop_duplicates('doi', inplace=True)
df_all[['data_add', 'title', 'abstract', 'Publication date',
       'doi', 'source_link']].to_csv('biorxiv_all.csv.gz', sep='\t')
