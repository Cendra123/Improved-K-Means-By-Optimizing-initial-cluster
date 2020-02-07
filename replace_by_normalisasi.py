import pandas as pd

import re

import sys


# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

tweet_hasil_normalisasi = []

if __name__ == '__main__':
	title_changed_xls = "Normalisasi_Term_02.xlsx"
	data_change = pd.read_excel(title_changed_xls)
	print(data_change)
	# print(data_change[(data_change['Term']=="memakan")]['Changed'])

	title_xls = "hasil_removing_ASCII_02.xlsx"
	data = pd.read_excel(title_xls)
	# print(data['Tweet'])

	for tweet in data['Tweet']:
		# print(tweet)
		tweet = re.sub(r" +"," ",tweet)
		texts_of_tweet = tweet.rstrip().lstrip().split(" ")
		# print(texts_of_tweet)
		texts_of_tweet_result = ""

		# print(texts_of_tweet)
		# sys.exit()
		for text_of_tweet_i in texts_of_tweet:
			# print(text_of_tweet_i)
			array_of_changed = data_change[(data_change['Term']==text_of_tweet_i.lower())]['Changed'].tolist()
			changed_tweet = ""
			
			if(len(array_of_changed)==1):
				changed_tweet = array_of_changed[0]
				print(changed_tweet)
			else:
				changed_tweet = text_of_tweet_i
			# else:
				# changed_tweet = text_of_tweet_i

			# print(changed_tweet)
			texts_of_tweet_result += changed_tweet+" "
		# print(texts_of_tweet_result.rstrip())
		# sys.exit()
		# print("asal: ", texts_of_tweet)
		# print("hasil: ",texts_of_tweet_result)
		tweet_hasil_normalisasi.append(texts_of_tweet_result)
	# sys.exit()
	tweet_hasil_normalisasi_df = pd.DataFrame(tweet_hasil_normalisasi)
	tweet_hasil_normalisasi_df.to_excel("hasil_tweet_normalisasi_02.xlsx", sheet_name="normalisasi")






	