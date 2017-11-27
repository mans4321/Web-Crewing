from collections import defaultdict
import json
import operator
import Index
import sys
from Index import readIndex
from Index import Index


def spimi_invert(token_stream, block_size, file_number, score):
    index = Index(score)

    while sys.getsizeof(dict) < block_size and len(token_stream) > 0:
        token = token_stream.pop(0)
        index.addTerm(token.term, token.docid)

    sorted_dict = sorted(index.getdictionary().keys(), key=operator.itemgetter(0))
    filename = 'mergeIndex/file' + str(file_number) + '.json'
    save_dict(filename, sorted_dict, index.getdictionary())
    print(sorted_dict)
    return filename


def save_dict(filename, sorted_dict, dict):
    print('----------------------------------------------')
    file = open(filename, 'w')
    for k in sorted_dict:
        termInf = dict[k]
        list = []
        list.insert(0, k)
        list.insert(1, termInf.semVaule)
        list.insert(2, termInf.dtf)
        term_detaile = json.dumps(list)
        str_termDict = json.dumps(termInf.docDict)
        file.write(term_detaile)
        file.write('\t')
        file.write(str_termDict)
        file.write('\n')
        file.flush()
    file.close()


def merge_postings(filesNameList, score):
    if len(filesNameList) == 1:
        return readIndex(filesNameList[0], score)
    else:
        index = readIndex(filesNameList[0],score)
        for n in range(1,len(filesNameList)):
            index.merge(index, readIndex(filesNameList[n]))
