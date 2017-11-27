import json


class TermInfo:

    def __init__(self, semVaule):
        self.semVaule = semVaule
        self.dtf = 0
        self.docDict = {}

    def addDoc(self, docID):
        freq = 0
        if docID in self.docDict:
            freq = self.docDict[docID]
        else:
            self.dtf += 1
        self.docDict[docID] = freq + 1

    def docFreq(self, docID):
        if docID in self.docDict:
            return self.docDict[docID]
        return None

    def setInfo(self, dtf, docDict):
        self.docDict = docDict
        self.dtf = dtf

    def setMergeInfo(self, termInfo):
        for k in termInfo.docDict:
            freq = 0
            if k in self.docDict:
                freq = termInfo.docDict[k]
            else:
                self.dtf += 1
            self.docDict[k] = termInfo.docDict[k] + freq


class Index:

    def __init__(self, score):
        self.dictionary = {}
        self.score = score

    def addTerm(self,term, docId):
        if term in self.dictionary:
            self.dictionary[term].addDoc(docId)
        else:
            sor = 0
            if term.lower() in self.score:
                sor = self.score[term.lower()]
            termInfo = TermInfo(sor)
            termInfo.addDoc(docId)
            self.dictionary[term] = termInfo

    def getSentiment(self, term):
        if term in self.dictionary:
            return self.dictionary[term].semVaule
        else:
            return 0

    def getDocFreq(self, term, docID):
        if term in self.dictionary:
            return self.dictionary[term].docFreq(docID)
        else:
            return None

    def getTermDtf(self, term):
        if term in self.dictionary:
            return self.dictionary[term].dtf
        else:
            return None

    def get_doc_list(self, term):
        results = []
        if term in self.dictionary:
            for key in self.dictionary[term].docDict:
                results.append(key)
        return results

    def getdictionary(self):
        return self.dictionary

    def merge(self, index):
        for k in index.getdictionary():
            if k in self.getdictionary():
                self.dictionary[k].setMergeInfo(index.getdictionary()[k])
            else:
                self.dictionary[k]= index.getdictionary()[k]


def storeIndex(fileName, indexObj):
    file = open(fileName, 'w')
    for k in indexObj.getdictionary():
        termInf = indexObj.getdictionary()[k]
        list = []
        list.insert(0,k)
        list.insert(1, termInf.semVaule)
        list.insert(2, termInf.dtf)
        term_detaile = json.dumps(list)
        termDict = json.dumps(termInf.docDict)
        file.write(term_detaile)
        file.write('\t')
        file.write(termDict)
        file.write('\n')
        file.flush()
    file.close()


def readIndex(filename, score):
    score = score
    index = Index(score)
    with open(filename, 'r')as f:
        for line in f:
            termDetail, termDict = line.split('\t')
            termDetail = json.loads(termDetail)
            termDict = json.loads(termDict)
            termInfo = TermInfo(termDetail[1])
            termInfo.setInfo(termDetail[2],termDict)
            index.getdictionary()[termDetail[0]] = termInfo

    return index

def dictFromSentimentFile():
    file = open("../Index/AFINN-111.txt", 'r')
    scores = {}
    for line in file:
        term, score = line.split('\t')
        scores[term] = int(score)
    file.close()
    # print scores.items()
    return scores


def get_index():
    score = dictFromSentimentFile()
    index = readIndex("../Index/loadIndex.json",score)
    return index
