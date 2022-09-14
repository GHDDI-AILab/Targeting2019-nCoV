import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os
import sys
import glob
from nltk.corpus import stopwords
import datetime

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import pickle

import spacy
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

## STOP WORDS =============================================================================
from stop_words import get_stop_words
stop_words = get_stop_words('en')
stop_words = get_stop_words('english')
stop_words.extend(['xa', 'use', 'com', 'https', 'http', 'org', 'gov'])
## ========================================================================================

#dataloader, load same way as other nlp script for now (change to database later)
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
#df5 = pd.read_csv('dimensions_papers.csv.gz', delimiter='\t')
'''
#desktop version - use this dataloader instead
df1 = pd.read_csv('/Users/jinyutong/Documents/cluster/2020-09-09/pubmed.csv', delimiter='\t')
df2 = pd.read_csv('/Users/jinyutong/Documents/cluster/biorxiv_all-1.csv.gz', delimiter='\t')
df3 = pd.read_csv('/Users/jinyutong/Documents/cluster/2020-09-09/chemrxiv.csv', delimiter='\t')
df4 = pd.read_csv('/Users/jinyutong/Documents/cluster/2020-09-09/arxiv.csv', delimiter='\t')
'''
df = pd.concat([df1, df2, df3, df4]) #,df5])
print(df.shape)
## ========================================================================================

## DATA PREPROCESSING =====================================================================
#remove entries without abstracts
def df_preprocess(df):
    df['doi'] = df['doi'].str.lower()
    df['doi'] = df['doi'].str.replace("'", '')
    df = df.drop_duplicates('doi')

    df['title'] = df['title'].str.lower()
    df['title'] = df['title'].str.replace("'", '').replace('.', '')
    df = df.drop_duplicates('title')

    df = df[df['abstract'].notna()]
    df = df[df['abstract']!='None']
    df = df.drop_duplicates('abstract')
    
    df.fillna('none', inplace=True)
    for i in range(0, len(df)):
        s1 = str(df['abstract'].iloc[i]).lower()
        df['abstract'].iloc[i] = s1.replace('\\n', ' ').replace('<sub>', '').replace('</sub>', '').replace('sars-cov', 'sars_cov')

    df['strlength'] = [len(abss) for abss in list(df['abstract'])]
    df = df[df['strlength']>200]

    return df

def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True)) 

def data_processor(all_text):
    bigram = gensim.models.Phrases(all_text, min_count=10, threshold=75)
    bigram_model = gensim.models.phrases.Phraser(bigram)

    trigram = gensim.models.Phrases(bigram[all_text], threshold=75)
    trigram_model = gensim.models.phrases.Phraser(trigram)

    all_text_ns = [[word for word in simple_preprocess(str(docs)) if word not in stop_words] for docs in all_text]
    all_text_ns_b = [bigram_model[docs] for docs in all_text_ns]
    all_text_ns_bt = [trigram_model[bigram_model[doc]] for doc in all_text_ns_b]
    
    all_text_p = []
    for texts in all_text_ns_bt:
        all_text_p.append([word.lemma_ for word in nlp(" ".join(texts))])

    dictionary = corpora.Dictionary(all_text_p)
    corpus = [dictionary.doc2bow(text) for text in all_text_p]
    
    return all_text_p, dictionary, corpus        
        
#df = df_preprocess(df)
#all_text = list(sent_to_words(list(df['abstract'])))
#all_text_p, dictionary, corpus = data_processor(all_text)

def lda_inference_process(filepath, dictionary):
    if type(filepath) is str:
        df = pd.read_csv(filepath)
    else:
        df = filepath
    print("文本预处理")
    df = df_preprocess(df)
    all_text = list(sent_to_words(list(df['abstract'])))
    all_text_p, _, _ = data_processor(all_text)
    print("词袋模型的 文档-单词矩阵")
    texts = [dictionary.doc2bow(text) for text in all_text_p]    # use existing dictionary for bag-of-words
    print("计算完成")

    return df, texts

## INFERENCING ========================================================================
def tm_generate_report(df, zzz, method='inference'):
    dictionary = pickle.load(open('covid-dict'+str(zzz)+'s.pkl', 'rb'))
    ldamodel = pickle.load(open('covid-lda-output'+str(zzz)+'s.pkl', 'rb'))
    #corpus = pickle.load(open('covid-texttfidf-output'+str(zzz)+'s.pkl', 'rb'))
    if method=='inference':
        print('Performing', method)
        all_text_p = pickle.load(open('covid-alltextps.pkl', 'rb'))
        texts = pickle.load(open('covid-text_output'+str(zzz)+'s.pkl', 'rb'))
    
    else:
        print('Predicting from other data')
        df, texts = lda_inference_process(df, dictionary)
        

    topic_dist = []
    scores = []
    topic_counts = []
    for i in range(0, len(texts)):
        topic_dist.append(np.argmax(list(ldamodel.inference([texts[i]])[0][0])))
        scores.append(np.max(list(ldamodel.inference([texts[i]])[0][0])))
    for j in range(0, zzz):
        topic_counts.append(topic_dist.count(j))
        print('Topic', str(j), 'count:', topic_dist.count(j))
    
    if method!='inference':
        topic_counts = []
    else:
        pickle.dump(topic_counts, open("topic_count.pkl","wb"))

    s1 = ldamodel.print_topics(num_topics=int(zzz), num_words=10)

    if method == 'inference':
        dftm = pd.DataFrame()
        for i in range(0, zzz):
            s2 = s1[i][1]
            s2 = s2.replace('*', '-').replace("\"", '').replace(' ', '')
            #print(s2.split('+'))
            topic = 'Topic' + str(i)
            dftm[topic] = s2.split('+')
        display(dftm)
        
    df_tt10 = []
    df.reset_index(drop=True)
    print(df.shape)
    print(len(topic_dist))
    df['topic'] = topic_dist
    df['tm_scores'] = scores
    df.reset_index(drop=True, inplace=True)
    for k in range(0, zzz):
        dfs1 = df[df['topic']==k].sort_values('tm_scores', ascending=False).reset_index(drop=True)
        print('Topic', k)
        #display(dfs1.head(10))
        df_tt10.append(dfs1[['Publication date', 'abstract', 'data_add', 'doi', 
                             'source_link', 'strlength', 'title', 'tm_scores', 'topic']].iloc[0:10, :])
        print('#####################################################')
    return df, topic_counts, topic_dist, scores, df_tt10

zzz=30
df, topic_counts, topic_dist, scores, df_tt10 = tm_generate_report(df, zzz, method='predict')

if len(topic_counts) == 0:
    topic_counts = pickle.load(open('topic_count.pkl', 'rb'))

    
#ldamodel = pickle.load(open('../cluster/covid_tm_10s/covid-lda-output'+str(zzz)+'s.pkl', 'rb'))
threshold = int(np.average(topic_counts)*0.2)

try:
    xl = pd.ExcelFile('covid_topicmodel_final.xlsx')
    tabs = xl.sheet_names
except:
    writer = pd.ExcelWriter('covid_topicmodel_final.xlsx', engine='xlsxwriter')
    for i in range(0, zzz):
        if topic_counts[i] > threshold:
            df_tt10[i][['Publication date', 'abstract', 'data_add', 'doi', 
                        'source_link', 'strlength', 'title', 'tm_scores', 'topic']].to_excel(writer, sheet_name=tabs[j], index=False)
            j+=1
        else:
            print('Topic', str(i), 'below topic model threshold!')
    writer.save()
    

j=0
blacklist = []
writer = pd.ExcelWriter('covid_topicmodel_new.xlsx', engine='xlsxwriter')
for i in range(0, zzz):
    if topic_counts[i] > threshold:
        df_tt10[i][['Publication date', 'abstract', 'data_add', 'doi', 
                    'source_link', 'strlength', 'title', 'tm_scores', 'topic']].to_excel(writer, sheet_name=tabs[j], index=False)
        j+=1
        
    else:
        blacklist.append(i)
        print('Topic', str(i), 'below topic model threshold!')
writer.save()

try:
    writer = pd.ExcelWriter('covid_topicmodel_final.xlsx', engine='xlsxwriter')
    w1 = pd.ExcelWriter('covid_topicmodel_final_newest.xlsx', engine='xlsxwriter')
    for tab in tabs:
        df1 = pd.read_excel('covid_topicmodel_final.xlsx', sheet_name=tab)
        df2 = pd.read_excel('covid_topicmodel_new.xlsx', sheet_name=tab)
        df1 = pd.concat([df2,df1]).drop_duplicates('doi').head(10)
        df1[['Publication date', 'abstract', 'data_add', 'doi', 
             'source_link', 'strlength', 'title', 'tm_scores', 'topic']].to_excel(writer,
                                                                                  sheet_name=tab, index=False)
        df3 = pd.concat([df1,df2]).drop_duplicates('doi').sort_values('data_add', ascending=False).head(10)
        df3[['Publication date', 'abstract', 'data_add', 'doi',
             'source_link', 'strlength', 'title', 'tm_scores', 'topic']].to_excel(w1,
                                                                                  sheet_name=tab, index=False)
    writer.save()
    w1.save()
except:
    print('New file')
    sys.exit() #require manual topic labels
today = str(datetime.date.today().strftime('%B %d, %Y'))
# WRITE HTML ================================================================================
htmlfile = open("ldatopics.html", "w")
m = htmlfile.write('''<!DOCTYPE html>
<html>

Last Updated: ''' +today+ '''

<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
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
</style>
</head>
<body>

<p>Click on the topic labels inside the tabbed menu:</p>

<div class="tab">\n''')

for i in range(0, len(tabs)):
    m1 = htmlfile.write('''  <button class="tablinks" onclick="openCity(event,'''+"'"+tabs[i]+"'"+''')">'''+tabs[i]+'''</button>\n''')
    
m2 = htmlfile.write('''</div>\n''')

a1 = htmlfile.write('''<!-- Tab content -->\n''')
for i in range(0, len(tabs)):
    df7 = pd.read_excel('covid_topicmodel_final.xlsx', sheet_name=tabs[i])
    df_html = df7[['title', 'doi']].to_html(index=False, justify='center')
   
    df_html = df_html.replace('<table border="1" class="dataframe">\n', '<table border=1 class="blueTable">\n <style>\n    @import url("blueTable.css");\n </style>\n')
    n0 = htmlfile.write('''<div id="'''+tabs[i]+'''" class="tabcontent">\n''')
    n = htmlfile.write(df_html)
    n1 = htmlfile.write('''</div>\n''')
    n2 = htmlfile.write('''\n''')

o1 = htmlfile.write('''
<script>
function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>
   
</body>
</html> 
''')
htmlfile.close()
print('HTML DONE')

'''
# DRAW FIGURES ================================================================
import datetime
all_topics_inference = []
month = int(datetime.date.today().strftime("%Y-%m")[-2:])

for i1 in blacklist:
    df = df[df['topic']!=i1]

def monthly_dataloader(df, month):
    df_x = df[df['Publication date'].str.contains('2020-'+str(month).zfill(2))]
    #texts_x = lda_inference_process(df_x, dictionary)
    #topic_dist = []
    #scores = []
    #for i in range(0, len(texts_x)):
        #topic_dist.append(np.argmax(list(ldamodel.inference([texts_x[i]])[0][0])))
        #scores.append(np.max(list(ldamodel.inference([texts_x[i]])[0][0])))
    
    topic_dist = list(df_x['topic'])
    monthly_topics = []
    for j in list(df[['topic']].sort_values('topic')['topic'].unique()):
        monthly_topics.append(topic_dist.count(j))
        print('Topic', str(j), 'count:', topic_dist.count(j))

    return monthly_topics

for i in range(1, month + 1):
    print('############# MONTH #############')
    print(i)
    monthly_topics = monthly_dataloader(df, i)

    all_topics_inference.append(monthly_topics)
    

months = list(range(1,month + 1))
all_topics_inference = np.array(all_topics_inference).T

plt.figure(figsize=(10,8))
for i in range(0, len(tabs)):
    plt.plot(months, all_topics_inference[i, :])
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Abstract Topic Counts per Month')
plt.legend(tabs)
plt.savefig('figure_nlp_tm1.png')

all_topics_total = all_topics_inference[:, :]
for i in range(1, month):
    all_topics_total[:, i] += all_topics_total[:, i-1]
plt.figure(figsize=(10,8))
for i in range(0, len(tabs)):
    plt.plot(months, all_topics_total[i, :])
plt.xlabel('Month')
plt.ylabel('Count')
plt.title('Cumulative abstract counts per topic')
plt.legend(tabs)
plt.savefig('figure_nlp_tm2.png')
print('Plots skipped')
'''
##update daily directly to the website (auto ssh)
import paramiko
from scp import SCPClient

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.connect('47.111.173.146', username='ghddirun', password='GHDDI@ali1')

with SCPClient(ssh.get_transport()) as scp:
    scp.put('ldatopics.html', '/home/ghddirun/github_covid19_web/Targeting2019-nCoV/') 
ssh.close()

print('Done')
