import pandas as pd

def get_symbols(market):
	symbols=[]
	df = pd.read_csv('allsymbols.dat', index_col=None, usecols=None, header=None, delimiter='\t')
	for i in range(1, len(df.index)):
		symbols.append(df.loc[i][0]+market)
	return symbols
