import TermInfo


class Index:
    dictionary = {}
    score = {}

    def __init__(self):
        file = open("AFINN-111.txt", 'r')
        self.score = self.dictFromSentimentFile(file)

    def addTerm(self,term, docId):
        if term in self.dictionary:
            self.dictionary[term].addDoc(docId)
        else:
            termInfo = TermInfo()
            sor = 0;
            if term.lower() in self.score:
                sor = self.score[term.lower()]
            termInfo.semVaule = sor
            termInfo.addDoc(docId)
            self.dictionary[term] = termInfo

    def getSentiment(self, term):
        if term in self.dictionary:
            return self.dictionary[term].semVaule
        else:
            return None

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



