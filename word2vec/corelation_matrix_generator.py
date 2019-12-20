import gensim
import time
import numpy as np
import pandas as pd

def Main():
	start=time.time()

	model = gensim.models.Word2Vec.load("VXV_NASDAQ_COMP")

	#arbitrary labels of the dataset to be created
	input_data=pd.read_csv("symbollist.csv", header=None, index_col=None)
	column_list = input_data[0].values.tolist()
	index_list = input_data[0].values.tolist()

	#dimensions of the vectors and the specified top n most correlated
	dimensions=400
	length=5


	#initialize matrix
	matrix = [[0 for x in range(len(column_list))] for y in range(len(index_list))]

	#initialize lists containing the vectors extracted from the model
	list_of_column_vectors=[[0 for x in range(dimensions-1)] for x in range(len(column_list))]
	list_of_index_vectors=[[0 for x in range(dimensions-1)] for x in range(len(index_list))]

	#add vectors to the lists
	for i in range(len(column_list)):
		print(str(column_list[i]))
		temp=model.wv[str(column_list[i]).lower()].tolist()
		temp2=model.wv[str(index_list[i]).lower()].tolist()
		list_of_column_vectors[i]=temp
		list_of_index_vectors[i]=temp2

	#perform a pearson correlation between each vector and add the result to the matrix in its respective position
	for i, column_word in enumerate(column_list):
		for j, index_word in enumerate(index_list):
			temp=np.corrcoef(list_of_column_vectors[i], list_of_index_vectors[j])[1, 0]
			print("Correlation between ", column_word.upper(), "and ", index_word.upper(), ": ", temp)
			if(temp>0.05):
				matrix[i][j]=temp
			else:
				matrix[i][j]=0

	#save matrix to pandas dataframe
	print("Saving dataset to Pandas dataframe...")
	df=pd.DataFrame(matrix, columns=column_list, index=index_list)


	#find the top n correlated vectors and list them by their label
	print("Finding top n for each company...")
	top_matrix=[[0 for x in range(length)] for y in range(len(column_list))]
	for i, column in enumerate(df.columns):
		top=df.nlargest(length, column)
		for l in range(length):
			top_matrix[i][l]=top.index.values[l]

	#transpose the matrix for easier reading
	print("Transponsing matrix")
	top_matrix=list(map(list, zip(*top_matrix)))

	#save as pandas dataframe
	print("Saving dataset as Pandas dataframe")
	df_top=pd.DataFrame(top_matrix, columns=column_list)


	#save to .csv files
	print("Saving files to .csv")
	df.to_csv("correlation_matrix.csv", index=True)
	df_top.to_csv("top_matrix.csv", index=True)
	end=time.time()
	print("Done. Elapsed time ", end-start)

	if __name__ == '__main__':
		Main()