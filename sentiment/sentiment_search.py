import json
import mmap
from index import get_index
import operator


# function retrieves all of the documents that contain the words in the query
def get_docs_containing_word(inverted_index, words):
	result = []
	for word in words:
		word_indexes = inverted_index.get_doc_list(word)
		for idx in word_indexes:
			if idx not in result:
				result.append(idx)

	return result


# function calculates total sentiment for a query string
def get_query_sentiment(inverted_index, words):
	sentiment_score = 0

	# iterate through tokens in query
	for token in words:
		sentiment_score += inverted_index.getSentiment(token)	
	return sentiment_score


# function calculates the total sentiment of the document
def get_document_sentiment(inverted_index, document_content):
	sentiment_score = 0
	if document_content != None:
		doc_words = document_content.split()

		for word in doc_words:
			sentiment_score += inverted_index.getSentiment(word)
	return sentiment_score


index = get_index()
#print(index.getDocFreq('jmsb','http://cufa.net'))


continue_queries = True

while continue_queries:
	query = input("Enter the word or words you are looking for. Leave the field blank to stop: ")
	if query != "":

		doc_ranked = {}
		words = query.split()
		query_sentiment = get_query_sentiment(index, words)
		print("\nQuery sentiment: " + str(query_sentiment) + "\n")
		doc_unranked = get_docs_containing_word(index, words)
		for doc in doc_unranked:
			with open("../Index/tokenized_docs.txt", "r") as f:
				value = None
				start_seen = False
				for line in f:
					if line.strip() == doc:
						start_seen = True
						continue

					if "<>" in line and start_seen:
						value = line
						break
			doc_sentiment = get_document_sentiment(index, value)
			doc_ranked[doc] = doc_sentiment

		# display results from most positive to least
		if query_sentiment >= 0:
			for key, value in sorted(doc_ranked.items(), key=operator.itemgetter(1), reverse=True):
				print("%s: %s" % (key, doc_ranked[key]))
		# display results from most negative to least
		else:
			for key, value in sorted(doc_ranked.items(), key=operator.itemgetter(1), reverse=False):
				print("%s: %s" % (key, doc_ranked[key]))
		print("\n")
	else:
	  print('Thank you. Have a nice day')
	  continue_queries = False
