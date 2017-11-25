class TermInfo:

    semVaule = 0
    dtf = 0
    docDict = {}

    def addDoc(self,docID):
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
