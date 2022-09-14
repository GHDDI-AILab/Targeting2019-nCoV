import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import re
import spacy
import ast

import os
import datetime
import glob


#try/except/else for loading 3 csv files, dimension.ai separate because of semi-weekly updated dataset
#8/25/2020: biorxiv json limited to 100 most recent papers, use aggregating function to get all downloaded papers
filelist = list(glob.glob('../outputcsv/*'))
filelist.sort(reverse=True)
file=False
i=0
while file is False:
    f1 = glob.glob(filelist[i]+'/*.csv')
    if filelist[i]+'/pubmed.csv' in f1:
        try:
            df1 = pd.read_csv(filelist[i]+'/pubmed.csv', delimiter='\t')
            file = True
            print('pubmed',filelist[i])
        except:
            file=False
            i += 1
    else:
        i += 1
        file = False

file = False
i=0
while file is False:
    f1 = glob.glob(filelist[i]+'/*.csv')
    if filelist[i]+'/chemrxiv.csv' in f1:
        try:
            df3 = pd.read_csv(filelist[i]+'/chemrxiv.csv', delimiter='\t')
            file = True
            print('chemrxiv',filelist[i])
        except:
            file=False
            i += 1
    else:
        i += 1
        file = False

file = False
i=0
while file is False:
    f1 = glob.glob(filelist[i]+'/*.csv')
    if filelist[i]+'/arxiv.csv' in f1:
        try:
            df4 = pd.read_csv(filelist[i]+'/arxiv.csv', delimiter='\t')
            file = True
            print('arxiv',filelist[i])
        except:
            file=False
            i+=1
    else:
        i += 1
        file = False

df2 = pd.read_csv('biorxiv_all.csv.gz', delimiter='\t')
df5 = pd.read_csv('dimensions_papers.csv.gz', delimiter='\t')

df = pd.concat([df1, df2, df3, df4, df5])
print(df.shape)

## Data preprocessing
#drop based on doi then title
df.drop_duplicates('doi', inplace=True)


df['title1'] = df['title'].str.lower()
df.drop_duplicates('title1', inplace=True)

df['abstract1'] = df['abstract'].str.lower()
df.fillna('\n', inplace=True)
df.drop_duplicates(['abstract1', 'title1'], inplace=True)

# filter and get all containing coronavirus related words
df_s1 = df[df['title1'].str.contains('covid')]
df_s2 = df[df['title1'].str.contains('coronavirus')]
df_s3 = df[df['title1'].str.contains('sars-cov')]
df_s4 = df[df['abstract1'].str.contains('covid')]
df_s5 = df[df['abstract1'].str.contains('coronavirus')]
df_s6 = df[df['abstract1'].str.contains('sars-cov')]
df = pd.concat([df_s1, df_s2, df_s3, df_s4, df_s5, df_s6]).drop_duplicates()
df.sort_values(by='data_add', ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)
print('Number of abstracts used', len(df))


for i in range(0, len(df)):
    s1 = str(df['abstract1'].iloc[i]).replace('(', '( ').replace(')', ' ) ').replace('/', ' ').replace('+', ' + ').replace('-', ' - ').replace('\n', ' ').replace('\\n', ' ').replace(',', ' , ').replace('\\xa0', ' ').replace('\\t', ' ').replace('Œº', 'u').replace('¬µ', 'u').replace('µ', 'u')
    # universally replace micro symbol with u , remove noise for next step
    df['abstract1'].iloc[i] = ' ' + s1 + ' '

df.sort_values(by='data_add', ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)


# import druglist for rule-based data extraction
druglist = pd.read_excel('nlp_drug_disease.xlsx', sheet_name=1)
druglist['DRUG_NAME'] = druglist['DRUG_NAME'].str.lower()
druglist['length'] = [len(str(x)) for x in druglist['DRUG_NAME'].tolist()]
druglist.dropna(inplace=True)
druglist = druglist[druglist['length'] >= 5] #from kaggle, keep only names >5


#get keywords related to preclinical, invitro, etc
ct_idx = []
drug = []
drugcount = []
dates = []
idx = []
sentences = []

preclinical = ['ec50', 'ic50', 'cc50'] #keywords
for i in range(0, len(df)):
    s1 = list(dict.fromkeys(df['abstract1'].iloc[i].split(' ')))
    s2 = list(set(s1) & set(preclinical))
    if len(s2) > 0:
        sentence = []
        for j in range(0, len(s2)):
            sentence.append(re.findall(r"([^.]*?"+s2[j]+"(?:[^\.]|\.(?=\d))*\.)", df['abstract1'].iloc[i]))
        sentences.append(sentence)
        ct_idx.extend(s2)
        drugcount.append(1)
        dates.append(df['title'].iloc[i])

        idx.append(i)

df2 = df.iloc[idx, :].reset_index(drop=True)
df2['sentence'] = sentences
df2.to_csv('01PRECLINICAL_allsentences.csv', index=False)
df2 = []
df2 = pd.read_csv('01PRECLINICAL_allsentences.csv')
print('Invitro abstracts:', len(df2))
###############################################################

# Extract treatments from df2
ct_idx = []
drug = []
drugcount = []
dates = []
idx = []
sentences = []

for i in range(0, len(df2)):
    s1 = list(dict.fromkeys(df2['abstract1'].iloc[i].split(' ')))
    s2 = list(set(s1) & set(list(druglist['DRUG_NAME'])))
    if len(s2) > 0:
        sentence = []
        for j in range(0, len(s2)):
            sentence.append(re.findall(r"([^.]*?" + s2[j] + "[^.]*\.)", df2['abstract1'].iloc[i]))
        sentences.extend(sentence)
        ct_idx.extend(s2)
        drugcount.append(1)
        dates.append(df['title'].iloc[i])

        idx.extend([i]*len(s2))

list_title = list(df2['title'].iloc[idx])
dois = list(df2['doi'].iloc[idx])
iv_evidence = list(df2['sentence'].iloc[idx])
df3 = pd.DataFrame(data={'drug':ct_idx, 'sentence':sentences, 
                         'title':list_title, 'doi':dois,
                         'in-vitro evidence':iv_evidence})
df3.drop_duplicates(['drug', 'title']).to_csv('02PRECLINICAL_title_iv_drugs.csv', index=False)

###############################################################

def nlp_rule1(str1):
    
    str1 = str1.replace('>', ' > ').replace('<', ' < ').replace('=', ' = ').replace('  ', ' ')
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(str1)

    i1 = str1.find('ec50')
    i2 = 'ec50'
    if i1 == -1:
        i1 = str1.find('ic50')
        i2 = 'ic50'

    nouns = []
    for nps in doc.noun_chunks:
        nouns.append(nps.text)

    for i in range(0, len(nouns)):
        i3 = nouns[i].find(i2)
        if i3 != -1:
            i4 = i
        else:
            pass

        if 'concentration' in nouns[i]:
            i5 = i
        elif 'molar' in nouns[i]:
            i5 = i
        else:
            pass
    try:        
        if i5 > i4: #quantitative description
            s4 = nouns[i5]
            s4 = str(re.findall(r"(\w+(?=\s+("+s4+")))", str1)[0][0]) + ' ' + s4            
            s3 = [i2, s4]
        elif i5 == i4: #adjective description
            s3 = [i2, nouns[i5]]

        else:
            s3 = [i2, 'not found']
    except:
        s3 = [i2, 'not found']
    return s3

def nlp_rule2(str1):
    #following ec50/ic50, jump 1-2 words and find numerical value (>,<,=,'of', 'at', 'around'), number may end with '*m'
    i1 = str1.find('ec50')
    i2 = 'ec50'
    if i1 == -1:
        i1 = str1.find('ic50')
        i2 = 'ic50'


    s3 = str1[i1:].replace('>', ' > ').replace('<', ' < ').replace('=', ' = ').replace('  ',
                    ' ').replace('ec50 )', 'ec50').replace('ic50 )', 'ic50').split(' ')

    if any(c in s3[1] for c in ('>', '<', '=', 'of', 'at', 'around', ',')):
        try:
            s4 = [i2, s3[2]]
        except:
            s4 = [i2, 'not found']
    elif s3[1] in ['value', 'values', 'concentration', 'concentrations', 'activity', 'activities']:
        try:
            s4 = [i2, s3[3]]
        except:
            s4 = [i2, 'not found']
    else:
        s4 = [i2, 'not found']
    return s4
    
def nlp_rule3(str1):
    i1 = str1.find('ec50')
    i2 = 'ec50'
    if i1 == -1:
        i1 = str1.find('ic50')
        i2 = 'ic50'

    s3 = str1.replace('  ', ' ').split(' ')
    i3 = -1
    for i in range(0, len(s3)):
        if i2 == s3[i]:
            i3 = i

    if i3 != -1:
        try:
            s4 = float(s3[i3+1])
        except:
            s4 = 'not found'
    if type(s4) is str:
        try:
            s4 = float(s3[i3-1])
        except:
            s4 = 'not found'
    return [i2, s4]

def nlp_rule4(str1):
    i1 = str1.find('ec50')
    i2 = 'ec50'
    if i1 == -1:
        i1 = str1.find('ic50')
        i2 = 'ic50'
        
    s3 = str1[i1:].replace('3c', 'three-c')
    
    s4 = []
    if re.search('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', s3) is not None:
        for catch in re.finditer('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', s3):
            if str(catch[0]) not in ['50', '90', '2', '6', '2019', '2020', '19']:
                s4.append(catch[0])
    else:
        s4 = 'not found'
    
    return [i2, s4[0]]

################################################################
# Specific data extraction 

df4 = pd.read_csv('02PRECLINICAL_title_iv_drugs.csv')
sent = []
param = []
r1 = []
r2 = []
r3 = []
r4 = []
i1 = []
doi = []
for i in range(0, len(df4)):
    s0 = ast.literal_eval(df4['in-vitro evidence'].iloc[i])
    s0 = [item for sublist in s0 for item in sublist]
    doi.extend([df4['doi'].iloc[i]]*len(s0))
    for j in range(0, len(s0)):
        s1 = str(s0[j]).replace('um', ' um').replace('μ', ' u').replace('nm', ' nm').replace(' m.', ' um ').replace('  ', ' ')
        sent.append(s1)
        try:
            s3 = nlp_rule3(s1)
            param.append(s3[0])
        except:
            s3 = 'not found'
            param.append('ec50')
        
        r3.append(s3[1])

        try:
            s3 = nlp_rule2(s1)[1]
        except:
            s3 = 'not found'
        r2.append(s3)

        try:
            s3 = nlp_rule1(s1)[1]
        except:
            s3 = 'not found'
        r1.append(s3)    

        try:
            s3 = nlp_rule4(s1)[1]
        except:
            s3 = 'not found'
        r4.append(s3)
        i1.append(i)
            
df_extract = pd.DataFrame(data={'sentidx':i1, 'sentence':sent, 
                                'parameter':param, 'rule1':r1, 'doi':doi,
                                'rule2':r2, 'rule3':r3, 'rule4':r4})
final_value = []
for i in range(0, len(df_extract)):
    #float(rule2)>rule3>rule4>rule1
    s1 = 'not found'
    if df_extract['rule2'].iloc[i] != 'not found':
        try:
            s1 = float(re.findall('[\d]+[.,\d]+|[\d]*[.][\d]+|[\d]+', df_extract['rule2'].iloc[i])[0])
            final_value.append(s1)
        except:
            s1 = 'not found'
    else:
        pass

    if (df_extract['rule3'].iloc[i] != 'not found') and (s1 == 'not found'):
        try:
            s1 = float(df_extract['rule3'].iloc[i])
            final_value.append(s1)
        except:
            s1 = 'not found'
    else:
        pass
    

    if (df_extract['rule4'].iloc[i] != 'not found') and (s1 == 'not found'):
        try:
            s1 = float(df_extract['rule4'].iloc[i])
            final_value.append(s1)
        except:
            s1 = 'not found'
    else:
        pass

    if s1 == 'not found':
        s1 = df_extract['rule1'].iloc[i]
        final_value.append(s1)

units = ['none']*len(final_value)
unit = [' um', ' nm', ' ug', 'micro', 'nano', 'mg/kg']
for i in range(0, len(final_value)):
    if len(str(final_value[i])) < 8:
        i1 = str(df_extract['sentence'].iloc[i]).find(df_extract['parameter'].iloc[i])
        s1 = df_extract['sentence'].iloc[i][i1:]
        for j in range(0, len(unit)):
            if unit[j] in s1:
                units[i] = unit[j]
                continue
    
df_extract['final_value'] = final_value
df_extract['units'] = units
df_extract.to_excel('03PRECLINICAL_all_ec50_extract.xlsx', index=False)

############################################################################################

#require df4 / df_extract
df4 = pd.read_csv('02PRECLINICAL_title_iv_drugs.csv')
df_extract = pd.read_excel('03PRECLINICAL_all_ec50_extract.xlsx')

ct_idx = []
for i in range(0, len(df_extract)):
    s1 = list(dict.fromkeys(df_extract['sentence'].iloc[i].split(' ')))
    s2 = list(set(s1) & set(list(druglist['DRUG_NAME'])))
    if len(s2) > 0:
        ct_idx.append(s2)
    else:
        ct_idx.append([None])

df_extract['drug'] = ct_idx
drug_mapping = []
#df_extract.drop_duplicates(['doi', 'drug', 'final_value'])
for doi in list(df4['doi'].unique()):
    s1 = list(df4[df4['doi']==doi]['drug'])
    l2 = list(df_extract[df_extract['doi']==doi]['drug'])
    if type(l2) is list:
        try:
            s2 = sum(l2, [])
        except:
            s2 = l2
    else:
        s2 = [None]
    new_drugs = list(set(s1).difference(set(s2)))
    drug_mapping.append([doi, new_drugs])

df5 = pd.DataFrame(drug_mapping).rename(columns={0:'doi', 1:'drug_x'})
df6 = pd.merge(df_extract, df5, on='doi', how='outer')

finallist1 = []
for i in range(0, len(df6)):
    for drugs in df6['drug'].iloc[i]:
        if drugs is not None:
            finallist1.append([drugs, df6['doi'].iloc[i], df6['parameter'].iloc[i], df6['final_value'].iloc[i], df6['units'].iloc[i], 'direct'])
    
    if df6['drug_x'].iloc[i] != []:
        for drugs in df6['drug_x'].iloc[i]:
            if drugs is not None:
                finallist1.append([drugs, df6['doi'].iloc[i], df6['parameter'].iloc[i], df6['final_value'].iloc[i], df6['units'].iloc[i], 'indirect'])

df7 = pd.DataFrame(finallist1).rename(columns={0:'Drug name', 1:'DOI', 2:'Assay', 3:'Value', 4:'Units', 5:'Correlation'}).drop_duplicates()
df7 = df7[df7['Value']!='not found']

print('Number of preclinical results:', len(df7))

################################# FORMATTING ##################################################
print('FORMATTING')
df7['Assay'] = df7['Assay'].str.replace('ec50', 'EC50').replace('ic50', 'IC50')
df7['DOI'] = df7['DOI'].str.replace('\'', '')

for i in range(0, len(df7)):
    if df7['Units'].iloc[i] == 'none':
        df7['Units'].iloc[i] = ""
    
    df7['Drug name'].iloc[i] = str(df7['Drug name'].iloc[i]).title()
    
df7 = df7.drop_duplicates(['Drug name', 'DOI'])
df7['Date Added'] = str(datetime.datetime.today().strftime("%Y%m%d"))
df7.to_csv('04PRECLINICAL_final_iv_druglist'+str(datetime.date.today()).replace('-', '')+'.csv', index=False)

print('length of df7: {}'.format(len(df7)))

#update: lookup historic data
print('update: lookup historic data')
df_h = pd.read_csv('05PRECLINICAL_historic_druglist.csv')
# df7['Date Added'] = str(datetime.datetime.today().strftime("%Y%m%d"))

print('length of historic: {}'.format(len(df_h)))

df7 = pd.concat([df_h, df7]).drop_duplicates(['Drug name', 'DOI', 'Assay', 'Correlation'], keep='last')

print('length of update dataframe after drop_duplicates: {}'.format(len(df7)))

df7 = df7.astype(object).where(pd.notnull(df7),None)
print('length of df_h: {}'.format(len(df_h)))
print('length of df7: {}'.format(len(df7)))
if len(df7) >= len(df_h):
    print("saving to {}".format("05PRECLINICAL_historic_druglist.csv"))
    df7.to_csv('05PRECLINICAL_historic_druglist.csv', index=False)

today = str(datetime.date.today().strftime('%B %d, %Y'))

#generate html
df_html = pd.concat([df7[df7['Correlation']=='direct'].sort_values('Drug name'), df7[df7['Correlation']=='indirect'].sort_values('Drug name')]).to_html(index=False, justify='center')
df_html = df_html.replace('<table border="1" class="dataframe">\n', '''<table border=1 class="blueTable">\n <style>\n    @import url("blueTable.css");\n
body {font-family: Arial;}
/* Style the tab */
.tab {
  overflow: hidden;
  border: 1px solid #ccc;
  background-color: #f1f1f1;
}

/* Style the buttons inside the tab */
.tab button {
  background-color: inherit;
  float: left;
  border: none;
  outline: none;
  cursor: pointer;
  padding: 10px 12px;
  transition: 0.3s;
  font-size: 12px;
}

/* Change background color of buttons on hover */
.tab button:hover {
  background-color: #ddd;
}

/* Create an active/current tablink class */
.tab button.active {
  background-color: #ccc;
}

/* Style the tab content */
.tabcontent {
  display: none;
  padding: 6px 10px;
  border: 1px solid #ccc;
  border-top: none;
} 
</style>\n''')

df_html = '''Last Updated: '''+today+ '''

<br>

''' + df_html 

#df_html.replace('''<td>None</td>''', '''<td> </td>''')

htmlfile = open("list.html", "w")
n = htmlfile.write(df_html)
htmlfile.close()



##update daily/weekly to server, embed html on website (auto ssh)
import paramiko 
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('47.111.173.146', username='ghddirun', password='GHDDI@ali1')

with SCPClient(ssh.get_transport()) as scp:
    scp.put('list.html', '/home/ghddirun/github_covid19_web/Targeting2019-nCoV/') #update to nginx server
ssh.close()

print('Done')

# %%
