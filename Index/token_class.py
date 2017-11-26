class Token:
    def __init__(self, term, docid):
        self.term = term
        self.docid = docid

    def __str__(self):
        return "Term: " + self.term + " docId: " + self.docid
