import json

with open('index.json') as data_file:
	index = json.load(data_file)
with open('tokenized_docs.json') as doc_file:
	tokenized_docs = json.load(doc_file)
continue_queries = True

while continue_queries:
	query = raw_input("Enter the word or words you are looking for. Leave the field blank to stop: ")
	if(query != ""):
		
		doc_ranked = {}
		words = query.split()
		query_sentiment = get_query_sentiment(index, words)
		
		doc_unranked = get_docs_containing_word(index, words)
		for doc in doc_unranked:
			doc_content = tokenized_docs[doc]
			doc_sentiment = get_document_sentiment(index, doc_content)
			doc_ranked[doc] = doc_sentiment

		# display results from most positive to least
		if query_sentiment >= 0:
			for key, value in sorted(doc_ranked.itervalues(), reverse=True):
				print "%s: %s" % (key, doc_ranked[key])
		# display results from most negative to least
		else:
			for key, value in sorted(doc_ranked.itervalues()):
				print "%s: %s" % (key, doc_ranked[key])
		
	else:
		print 'Thank you. Have a nice day'
		continue_queries = False


# function retrieves all of the documents that contain the words in the query	
def get_docs_containing_word(inverted_index, words):
    result = []
    for word in words:
        word_indexes = inverted_index[word][docDict]
        for idx in word_indexes:
            if idx not in result:
                result.append(idx)

    return result


# function calculates total sentiment for a query string
def get_query_sentiment(inverted_index, words):
	sentiment_score = 0
	
	# iterate through tokens in query
	for token in words:
		if token not in index:
			continue
		#possibly index[token][TermInfo][semValue] - needs testing with real json file
		sentiment_score += index[token][semValue]
		
	return sentiment_score
	

# function calculates the total sentiment of the document 
def get_document_sentiment(inverted_index, document_content):
	sentiment_score = 0
	doc_words = document_content.split()
	
	for word in doc_words:
		if word not in index:
			continue
		sentiment_score += index[token][semValue]
		
	return sentiment_score