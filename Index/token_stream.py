from file_access import open_file
from token_class import Token
from normalization import normalize
import json


# Next: normalization which will give a list of terms
# Normalization can include: case folding, number removal, stopword, stemming, Design Decisions(USA vs U-S-A)

def get_token_stream():
	tokenList = list()	# stream of Token objects(term and docId)
	doc_len_arr = []
	fileRead = open_file('../items.jl')
	documentList = create_parsed_text(fileRead)
	for doc in documentList:
		if doc.strip() == "":
			break
		docTermList, docID = parse_doc(doc)
		listofTokens = get_list_of_terms(docTermList, docID)
		tokenList.extend(listofTokens)
		fileOutput = " ".join(docTermList)
		file = open("tokenized_docs.txt", "a+")
		file.write(docID + "\n" + fileOutput + "<>\n")
		file.close()
	return tokenList


def create_parsed_text(file):
	return file.split('\n')


def parse_doc(line):
	token_list = []
	doc = json.loads(line)
	docID = doc['name'][0]
	docContent = doc['content']
	for sentence in docContent:
		sentence = sentence.replace('"', '')
		break_sentence = sentence.split()
		for word in break_sentence:
			token_list.append(word.strip().lower())
	return token_list, docID


def get_list_of_terms(tokenizedTermList, docId):
	token_list = list()
	# Loops through all the terms in the document and adds them to the list with their associated docId
	for term in tokenizedTermList:
		term = normalize(term)
		if term != '':
			tokenObj = Token(term, docId)
			token_list.append(tokenObj)
			#To remove duplicates uncomment the following
			#term_dict.append(term)
	return token_list


