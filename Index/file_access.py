import json

from token_class import Token
from normalization import normalize


def get_token_stream():
    tokenList = list()  # stream of Token objects(term and docId)
    fileRead = open_file('items.jl')
    for doc in fileRead:
        if doc.strip() == "":
            break
        docTermList = parse_doc(doc)
        tokenList.extend(docTermList)
        print(tokenList[4].term)
    return tokenList


def open_file(filename):
    fileOpen = open(filename, 'r')
    return fileOpen.read()


def parse_doc(doc):
    print(doc)
    term_list = []
    doc = json.loads(doc)
    docID = doc['name'][0]
    docContent = doc['content']
    for sentence in docContent:
        sentence = sentence.replace('"', '')
        break_sentence = sentence.split()
        for word in break_sentence:
            term_list.append(word.strip().lower())
    return get_list_of_terms(term_list,docID)


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
