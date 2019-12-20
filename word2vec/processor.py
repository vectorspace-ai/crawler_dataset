import pandas as pd
import sys
import re
import csv
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import logging
from gensim.models import word2vec
import multiprocessing




def Main():
	if len(sys.argv) != 2:
		print('*****')
		print("Must have a .csv as argument")
		print('*****')
		exit()

		
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',\
    level=logging.INFO)


	initial_corpus=sys.argv[1]

	processed_corpus=[]
	for i in range( 0, len(initial_corpus.index)):
		processed_corpus.append(corpus_processing(initial_corpus.iloc[i]['about_text']))
	
	final_corpus=tokenizer(processed_corpus)
	trainer(final_corpus)

def fix_csv(name):
	df=pd.read_csv(name)
	df['about_text'] = df['about_text'].shift(-1)
	df['name'] = df['name'].str.replace(r'.O$', '')
	df = df.dropna(subset=['about_text'])
	df = df[['name', 'about_text']]
	for i in range(len(df.index)):
		df.iloc[i]['about_text']=df.iloc[i]['name']+" "+df.iloc[i]['about_text']
	df.sort_values(by=['name'], inplace=True)
	df['name'].to_csv("symbollist.csv", index=None, header=None)	
	return df


def corpus_processing(dataframe):
	letters = re.sub("[^a-zA-Z]", " ", dataframe) 
	words = letters.split()
	no_dups = list(dict.fromkeys(words))
	stops = set(stopwords.words("english"))
	no_stop_words= [word for word in no_dups if not word in stops]
	clean_document=[i.lower() for i in no_stop_words]
	return( " ".join(clean_document))

def tokenizer(f):
	data = [] 
  
	# iterate through each sentence in the file 
	for i in f: 
		temp = [] 
      
		# tokenize the sentence into words 
		for j in word_tokenize(i): 
			temp.append(j.lower()) 
		data.append(temp)
	df=pd.DataFrame(data)
	df.to_csv("check.csv")
	return data
def trainer(corpus):
	print("training")
	model = word2vec.Word2Vec(corpus, size=400, window=10, min_count=1, workers=multiprocessing.cpu_count())
	model.init_sims(replace=True)
	model_name = "VXV_NASDAQ_COMP"
	model.save(model_name)

if __name__ == '__main__':
	Main()