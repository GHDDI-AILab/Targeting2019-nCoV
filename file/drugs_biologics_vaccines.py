import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from io import StringIO
from nltk import ngrams

from PIL import Image 
from wordcloud import WordCloud, STOPWORDS 

import random
import sys
import re
import os

import wget

def clinical_wordcloud(df, outputfile):
    ct_= str(list(df['Intervention'])).replace(', ', ' , ').replace('(', ' ').replace(')', ' ').replace("'", '').replace("[", '').replace("]", '')


    text = ct_
    stopwords = set(STOPWORDS)
    add_swords = 'none,biological,placebo,vaccine,drug,high,medium,low,phase,dose,day,schedule,regimen,treatment'.split(',')
    for s in add_swords:
        stopwords.add(s)

    wc = WordCloud(max_words=100, stopwords=stopwords, margin=10, random_state=6, width=800, height=400, background_color="white").generate(text)
    default_colors = wc.to_array()

    plt.imshow(default_colors, interpolation="bilinear")
    wc.to_file(outputfile)
    plt.axis("off")
    
    return None


dimensions_metadata = pd.read_csv('dimensions_metadata.csv')
dimensions_metadata['iteration'].iloc[0] = str(int(dimensions_metadata['iteration'].iloc[0])+1)

try:
    fn = wget.download('https://dimensions.figshare.com/ndownloader/articles/11961063/versions/'+dimensions_metadata['iteration'].iloc[0])
    #dimensions_metadata.to_csv('dimensions_metadata.csv', index=False)
    print('New Update!')    
except:
    print('no updates')
    sys.exit()

if fn[-3:] == 'zip':
    from zipfile import ZipFile
    with ZipFile(fn, 'r') as zipObj:
        filelist = zipObj.namelist()
        zipObj.extractall()
        
try:
    os.rename(filelist[-1], 'dimensions_excel.xlsx')
except:
    os.remove('dimensions_excel.xlsx')
    os.rename(filelist[-1], 'dimensions_excel.xlsx')
df = pd.read_excel('dimensions_excel.xlsx', sheet_name='Clinical Trials')
os.remove('11961063.zip') #remove to save space

today = str(datetime.date.today().strftime('%B %d, %Y'))

##########generate country plot

def dropna_col(df, col=None):
    df.reset_index(drop=True, inplace=True)
    if col is None:
        return df.dropna()
    else:
        df_s1 = df[[col]]
        indlist = list(df_s1.dropna().index)
        return df.loc[indlist]
        
#find country of sponsor, if multiple countries, count multiple times
a = list(df['Country of Sponsor/Collaborator'].unique())
b = [len(df[df['Country of Sponsor/Collaborator']==x]) for x in a]
df_cos = pd.DataFrame(data={'Country of Sponsor/Collaborator':a, 'count':b}).sort_values(by='count', ascending=False)

new_data = []
for i in range(0, len(df_cos)):
    s1 = str(df_cos.iloc[i,0]).find(';')
    stop = False
    while stop is False:
        s1 = str(df_cos.iloc[i,0]).find(';')
        if s1 == -1:
            stop = True
        else:
            s2 = df_cos.iloc[i,0][0:s1]
            df_cos.iloc[i,0] = df_cos.iloc[i,0][s1+2:]
            if s2 in df_cos.iloc[i,0]:
                stop = False
            else:
                new_data.append([s2, df_cos.iloc[i,1]])
df_new = pd.DataFrame(data=new_data, columns=['Country of Sponsor/Collaborator', 'count'])

df_cos = pd.concat([df_cos, df_new])
df_cos.reset_index(drop=True, inplace=True)

for name in list(df_cos['Country of Sponsor/Collaborator'].unique()):
    df_s1 = df_cos[df_cos['Country of Sponsor/Collaborator']==name]
    s1 = np.sum(df_s1['count'])
    df_cos['count'].loc[list(df_s1.index)] = s1
df_cos = df_cos.drop_duplicates(subset='Country of Sponsor/Collaborator').dropna()
        
df_cos.sort_values(by='count', ascending=False, inplace=True)
df_cos.reset_index(drop=False, inplace=True)
#remove for obvious reasons:
df_cos.drop(list(df_cos[df_cos['Country of Sponsor/Collaborator'].str.contains('Taiwan')].index), axis=0, inplace=True)
df_cos.drop(list(df_cos[df_cos['Country of Sponsor/Collaborator'].str.contains('Maca')].index), axis=0, inplace=True)

fig, ax = plt.subplots(figsize=(10,25))
bars = ax.barh(np.arange(len(df_cos)), df_cos['count'], 0.75)

ax.set_xlabel('Trial Count', fontdict={'fontsize': 16})
ax.set_title('Number of Clinical Trials on COVID-19 in each Country', fontdict={'fontsize': 16})
ax.set_yticks(np.arange(len(df_cos)))
ax.set_yticklabels(list(df_cos['Country of Sponsor/Collaborator']))#, rotation='vertical')
ax.set_ylabel(' ')
plt.gca().invert_yaxis()
plt.margins(0.05, 0.005)

max_x = ax.get_xlim()[1]
distance = max_x * 0.0025
for bar in bars:
    text = "{}".format(bar.get_width())
    text_x = bar.get_width() + distance
    text_y = bar.get_y() + bar.get_height()/2
    ax.text(text_x, text_y, text, va='center')

fig.savefig('figure_countries.png', bbox_inches='tight')


df1 = df #make copy of original dataframe
df1['Abstract'] = df1['Abstract'].str.lower()
df1['Brief title'] = df1['Brief title'].str.lower()
df1['Intervention'] = df1['Intervention'].str.lower()
df1.fillna(value='None', inplace=True)
df1.reset_index(drop=True, inplace=True)

#count of vaccines
df_v = pd.concat([df1[df1['Intervention'].str.contains('vaccine')], df1[df1['Brief title'].str.contains('vaccine')]]).drop_duplicates(subset='Trial ID')
print('Number of vaccine trials:', len(df_v))

##########lurong
df_v[["Trial ID","Title","Phase","Intervention"]].to_csv('vaccine.csv', index=False)


#count of biologics
df_i2 = pd.concat([df1[df1['Intervention'].str.contains('mab')], df1[df1['Intervention'].str.contains('biolog')], 
                   df1[df1['Abstract'].str.contains('mab')], df1[df1['Abstract'].str.contains('biolog')],
                   df1[df1['Intervention'].str.contains('antibod')], df1[df1['Abstract'].str.contains('antibod')],
                   df1[df1['Abstract'].str.contains('protein')], df1[df1['Intervention'].str.contains('cell')],
                   df1[df1['Abstract'].str.contains('cell')], df1[df1['Intervention'].str.contains('protein')], df1[df1['Intervention'].str.contains('plasma')]]).drop_duplicates(subset='Trial ID')

#remove vaccines from biologics
for i in range(0, len(df_v)):
    try:
        df_i2.drop(list(df_v.index)[i], axis=0, inplace=True)
    except:
        pass

#get clinical trials from 'mab' keyword
biologics = []
biologic_trials = []
for i in range(0, len(df_i2)):
    s1 = df_i2['Intervention'].iloc[i].replace(';', '').replace('(', '').replace(')', '').replace(',', '').replace('+', ' ').replace('-', ' ').replace('/', ' ').split()
    substring = 'mab'
    substring_in_list = list(dict.fromkeys([string for string in s1 if substring in string]))
    
    if substring_in_list != []:
        biologic_trials.append(i)
    biologics.extend(substring_in_list)

#get clinical trials based on key words
df_i3 = df_i2[df_i2['Intervention'].str.contains('cell')]
df_i4 = df_i2[df_i2['Intervention'].str.contains('plasma')]
df_i5 = df_i2.iloc[biologic_trials, :]

df_b = pd.concat([df_i3, df_i4, df_i5]).drop_duplicates(subset='Trial ID')
print('Number of biological drug trials:', len(df_b))

############lurong
df_b[["Trial ID","Title","Phase","Intervention"]].to_csv('biologics.csv', index=False)

###################DRUG LIST##############################################
druglist = pd.read_excel('nlp_drug_disease.xlsx', sheet_name=1)
druglist['DRUG_NAME'] = druglist['DRUG_NAME'].str.lower()
druglist['length'] = [len(str(x)) for x in list(druglist['DRUG_NAME'])]
druglist.dropna(inplace=True)
ct_idx = []
drug = []
drugcount = []
dates = []
idx = []

#from kaggle, keep only names >5
#own data analysis keep all strings <75 and classify as n-gram
druglist1 = druglist[druglist['length']>=5]
druglist1 = druglist1[druglist1['length']<=75]
druglist1['ngram'] = [len(str(x).split(' ')) for x in list(druglist1['DRUG_NAME'])]


df1['Intervention1'] = df1['Intervention'].str.lower()
for i in range(0, len(df1)):
    s1 = df1['Intervention1'].iloc[i].replace('(', '( ').replace(')', ' ) ').replace('/', ' ').replace('+', ' + ').replace('-', ' - ')
    df1['Intervention1'].iloc[i] = ' ' + s1 + ' '
    
df1.sort_values(by='Date added', ascending=False, inplace=True)

df1.drop(list(df1[df1['Intervention1'].str.contains('supplement')].index), axis=0, inplace=True)
df1.drop(list(df1[df1['Intervention1'].str.contains('traditional')].index), axis=0, inplace=True)
df1.drop(list(df1[df1['Intervention1'].str.contains('water')].index), axis=0, inplace=True)
df1.drop(list(df1[df1['Intervention1'].str.contains('vaccine')].index), axis=0, inplace=True)
df1.sort_values(by='Date added', ascending=False, inplace=True)
df1.reset_index(drop=True, inplace=True)

# list of 2 merged sets for unigram, bigram, and trigram to extract all drug names
for i in range(0, len(df1)):
    s1 = list(dict.fromkeys(df1['Intervention1'].iloc[i].split(' ')))
    s2 = list(set(s1) & set(list(druglist1['DRUG_NAME'])))
    if len(s2) > 0:
        ct_idx.append(str(s2).replace('[', '').replace(']', '').replace('\'', ''))
        drugcount.append(1)
        dates.append(df1['Date added'].iloc[i])
        if 'mab' in str(list(df1['Intervention1'].iloc[i])) and len(s2) <2:
            continue
        idx.append(i)        

n = 2
bigrams = []
for i in range(0, len(df1)):
    bigram = ngrams(str(df1['Intervention1'].iloc[i]).split(), n)
    blist = [" ".join(list(grams)) for grams in bigram]
    bigrams.append(blist)
    
druglist2 = druglist1[druglist1['ngram']==n]
ct_idx2 = []
drugcount = []
idx2 = []
for i in range(0, len(df1)):
    s1 = bigrams[i]
    s2 = list(set(s1) & set(list(druglist2['DRUG_NAME'])))
    if len(s2) > 0:
        ct_idx2.append(str(s2).replace('[', '').replace(']', '').replace('\'', ''))
        drugcount.append(1)
        #dates.append(df1['Date added'].iloc[i])
        idx2.append(i)

n = 3
trigrams = []
for i in range(0, len(df1)):
    trigram = ngrams(str(df1['Intervention1'].iloc[i]).split(), n)
    tlist = [" ".join(list(grams)) for grams in trigram]
    trigrams.append(tlist)
    
druglist3 = druglist1[druglist1['ngram']==n]
ct_idx3 = []
drugcount = []
idx3 = []
for i in range(0, len(df1)):
    s1 = trigrams[i]
    s2 = list(set(s1) & set(list(druglist2['DRUG_NAME'])))
    if len(s2) > 0:
        ct_idx3.append(str(s2).replace('[', '').replace(']', '').replace('\'', ''))
        drugcount.append(1)
        idx3.append(i)
        
df1['drug1'] = None
for a,b in zip(ct_idx, idx):
    df1['drug1'].iloc[b] = a
df1['drug2'] = None
for a,b in zip(ct_idx2, idx2):
    df1['drug2'].iloc[b] = a
df1['drug3'] = None
for a,b in zip(ct_idx3, idx3):
    df1['drug3'].iloc[b] = a
    
df2 = pd.concat([df1[df1['drug1'].notna()], df1[df1['drug2'].notna()], df1[df1['drug3'].notna()]]).drop_duplicates('Trial ID')[['Trial ID', 'drug1', 'drug2', 'drug3']]
df2.fillna('none', inplace=True)

print('Number of drugs (all) Trials:', len(df2))
#df_d = df1.loc[idx, :].drop_duplicates(subset='Trial ID').reset_index(drop=True)
#df_d2 = pd.DataFrame(data={'Treatment':ct_idx, 'Count':1}) #merged changes to column names

df2['count'] = 1
df2['drug_final'] = None

for i in range(0, len(df2)):
    #print(i)
    if df2['drug1'].iloc[i] is not None:
        s1 = str(df2['drug1'].iloc[i]).split(', ')
        for d in range(0, len(s1)):
            if s1[d] in str(df2['drug2'].iloc[i]):
                s1[d] = 'none'
        for r in range(0, len(s1)):
            if s1[r] in str(df2['drug3'].iloc[i]):
                s1[r] = 'none'
        df2['drug_final'].iloc[i] = list(set(s1)) + str(df2['drug2'].iloc[i]).split(', ') + str(df2['drug3'].iloc[i]).split(', ')
    else:
        df2['drug_final'].iloc[i] = str(df2['drug2'].iloc[i]).split(', ') + str(df2['drug3'].iloc[i]).split(', ')

treatments = [item for sublist in list(df2['drug_final']) for item in sublist]
df_d2 = pd.DataFrame(data={'Treatment':treatments, 'Count':1}) #merged changes to column names
df_d2 = df_d2[df_d2['Treatment']!='none'].reset_index(drop=True)
for all1 in list(df_d2['Treatment'].unique()):
    i1 = list(df_d2[df_d2['Treatment'] == all1].index)
    df_d2['Count'].loc[i1] = int(len(df_d2[df_d2['Treatment'] == all1]))
    
#create blacklist, some borrowed from kaggle list, keep 'mab' in final list
blacklist = ['plasma', 'serum', 'cell', 'biolog', 'vaccine', 'honey', 'injection', 'glucose', 'perform', 'ethanol', 'methanol', 'paraffin', 'soybean', 'horseradish', 'apple', 'ginger',' mouthwash', 'oregano', 'formaldehyde', 'alcohol', 'cannabis', 'cumin', 'tcm', 'piper', 'pepper', 'vitamin']

for words in blacklist:
    df_d2.drop(list(df_d2[df_d2['Treatment'].str.contains(words)].index), axis=0, inplace=True)

#change first letter to uppercase (for loop is most effective method, df[].str[0].upper() cannot batch operate)
for i in range(0, len(df_d2)):
    s1 = df_d2['Treatment'].iloc[i][0].upper()
    df_d2['Treatment'].iloc[i] = s1 + df_d2['Treatment'].iloc[i][1:]

dlistn = 'druglist_' + str(datetime.date.today()).replace('-', '') + '.csv'
df_d_clean=df_d2.drop_duplicates().sort_values(by='Treatment').sort_values(by='Count', ascending=False)
df_d_clean.to_csv(dlistn, index=False)
df_d_clean.sort_values(by='Treatment').to_csv('druglist.csv', index=False)

df_d = pd.merge(df1, df2[['Trial ID']], on='Trial ID', how='inner').drop_duplicates('Trial ID')
df_d[["Trial ID","Title","Phase","Intervention"]].to_csv('all_drugs.csv', index=False)

#df_d2.drop(list(df_d2[df_d2['drug'].str.contains('mab')].index), axis=0, inplace=True) #(let's add antibody)
print('Number of all drug trials (corrected):', len(df_d)) #after dropping keywords from blacklist

######lurong plot
ax = df_d_clean.plot.barh(figsize=(20, int(len(df_d_clean)/3.1)), x='Treatment', y='Count', color='green')
ax.invert_yaxis()
for i in ax.patches:
    ax.text(i.get_width()+.3, i.get_y()+.38, str(int(i.get_width())), fontsize=18, color='black')

ax.set_yticklabels(list(df_d_clean['Treatment']), fontdict={'fontsize':20})
plt.title('Number of clinical trials on each treatment ', fontdict={'fontsize':28})
plt.xlabel('Number of Clinical Trials', fontdict={'fontsize':20})
plt.ylabel(' ')
ax.get_legend().remove()
plt.savefig("figure_drugs_treatment.png", bbox_inches='tight')

####### pie plot - merged implementations
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
clinical_trial_type = ['Small Molecule Drugs', 'Biologics', 'Vaccines']
clinical_trial_count = [len(df_d), len(df_b), len(df_v)]
explode = (0, 0, 0.1)  # only "explode" the vaccine

fig, ax = plt.subplots(figsize=(8,8))

def func(pct, allvals):
    absolute = int(np.ceil(pct/100.*np.sum(allvals)))
    if absolute not in allvals:
        absolute -= 1
    return "{:.1f}%\n({:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(clinical_trial_count, labels=clinical_trial_type, 
                                  explode=explode, shadow=True, startangle=90,
                                  autopct=lambda pct: func(pct, clinical_trial_count),
                                  textprops={'fontsize':10}, radius=0.7)  
ax.set_title('Number of Trials in each Therapeutic Area', fontdict={'fontsize':14})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
fig.savefig('figure_types.png', bbox_inches='tight')

df_b = pd.read_csv('biologics.csv')
clinical_wordcloud(df_b, 'biologics_cloud.png')

df_v = pd.read_csv('vaccine.csv')
clinical_wordcloud(df_v, 'vaccine_cloud.png')

##update daily directly to the website (auto ssh)
import paramiko 
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('47.111.173.146', username='ghddirun', password='GHDDI@ali1')

with SCPClient(ssh.get_transport()) as scp:
    #update all figures and tables
    scp.put('druglist.csv', '/home/ghddirun/aidd-common-oss/file/druglist.csv') 
    scp.put('figure_countries.png', '/home/ghddirun/aidd-common-oss/file/figure_countries.png')
    scp.put('figure_drugs_treatment.png', '/home/ghddirun/aidd-common-oss/file/figure_drugs_treatment.png')
    scp.put('figure_types.png', '/home/ghddirun/aidd-common-oss/file/figure_types.png')
    scp.put('biologics.csv', '/home/ghddirun/aidd-common-oss/file/ct_biologics.csv')
    scp.put('vaccine.csv', '/home/ghddirun/aidd-common-oss/file/ct_vaccine.csv')
    scp.put('vaccine_cloud.png', '/home/ghddirun/aidd-common-oss/file/vaccine_cloud.png')
    scp.put('biologics_cloud.png', '/home/ghddirun/aidd-common-oss/file/biologics_cloud.png')
ssh.close()

##################################################################################################
#update preclinical dimensions dataset
dimensions = pd.read_excel('dimensions_excel.xlsx', sheet_name='Publications')
dimensions = dimensions[['Date added', 'Title', 'Abstract', 'Publication Date', 'DOI', 'Dimensions URL']]
dimensions.rename(columns={'Date added':'data_add', 'Title':'title', 'Abstract':'abstract', 
                           'Publication Date':'Publication date', 'DOI':'doi', 
                           'Dimensions URL':'source_link'},  inplace=True)
dimensions.to_csv('dimensions_papers.csv.gz', sep='\t', index=False)
print('Done')

############ UPDATE METADATA AFTER COMPLETION ###################
dimensions_metadata.to_csv('dimensions_metadata.csv', index=False) 
