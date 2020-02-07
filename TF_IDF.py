import pandas as pd

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

import sys
 

if __name__ == '__main__':
	titlexls = "hasil_normalisasi_Stopwords_02.xlsx"
	data = pd.read_excel(titlexls)
	print(data["Tweet"])

	#instantiate CountVectorizer()
	cv=CountVectorizer()

	# this steps generates word counts for the words in your docs
	word_count_vector=cv.fit_transform(data["Tweet"])

	# mendapatkan nama fitur
	word_list = cv.get_feature_names()

	# menjumlah frekuensi tiap fitur
	count_list = word_count_vector.toarray().sum(axis=0)
	data_frekuensi = dict(zip(word_list,count_list))

	# generate TF
	# term_frecuency_df = pd.DataFrame.from_dict(data_frekuensi, orient='index')
	# export TF
	# term_frecuency_df.to_excel("term_frecuency_01.xlsx", sheet_name="tf")

	# measure shape
	# print(word_count_vector.shape)
	
	tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)

	tfidf_transformer.fit(word_count_vector)

	# print idf values
	# df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(),columns=["idf_weights"])
	# sort ascending
	# df_idf.sort_values(by=["idf_weights"])


	# count matrix
	count_vector=cv.transform(data["Tweet"])
 
	# tf-idf scores
	tf_idf_vector=tfidf_transformer.transform(count_vector)

	feature_names = cv.get_feature_names()

	# print(tf_idf_vector.T.todense().index)
	# sys.exit()

	# place tf-idf values in a pandas data frame
	df = pd.DataFrame(tf_idf_vector.toarray(), columns=feature_names)
	print(df)

	df.to_excel("TF-IDF_normalisasi_02.xlsx", sheet_name="tfidf")

	
	sys.exit()