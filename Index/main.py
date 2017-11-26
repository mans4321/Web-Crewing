from token_stream import get_token_stream
from spimi import spimi_invert
from spimi import merge_postings
from Index import storeIndex
from Index import readIndex


def indexation():
    escape_layout = "----------------------------"
    score = dictFromSentimentFile()
    memory_size = None
    while not (isinstance(memory_size, (int, float))):
        try:
            memory_size = int(input("Enter the desired memory size: \n"))
        except:
            print("Please enter a number\n")
    print(escape_layout)
    print("Tokenizing")
    stream = get_token_stream()
    print("Documents Tokenized")
    print(escape_layout)
    file_name_list = list()
    print("Executing SPIMI")
    while len(stream) != 0:
        file_name = spimi_invert(stream, memory_size, len(file_name_list),score)
        file_name_list.append(file_name)
    print("SPIMI Completed")
    print(escape_layout)
    print("Merging Postings")
    index = merge_postings(file_name_list, score)
    storeIndex("loadIndex.json", index)
    print("Postings Merged")
    print(escape_layout)


def dictFromSentimentFile():
    file = open("Index/AFINN-111.txt", 'r')
    scores = {}
    for line in file:
        term, score = line.split('\t')
        scores[term] = int(score)
    file.close()
    # print scores.items()
    return scores


def getIndex():
    indexation()
    score = dictFromSentimentFile()
    index = readIndex("loadIndex.json",score)
    return index

index = getIndex()
print(index.getDocFreq('jmsb','http://cufa.net'))
