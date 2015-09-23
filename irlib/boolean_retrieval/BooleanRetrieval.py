# Boolean retrieval implemnets the slgorithms of the first chapter of the course boook

class InvertedIndex:
    """
    1. Collect the documents to be indexed: Friends, Romans, countrymen. So let it be with Caesar . . .
    2. Tokenize the text, turning each document into a list of tokens: Friend Romans countrymen
    3. Do linguistic preprocessing, producing a list of normalized tokens, which are the indexing terms:
    4. Index the documents that each term occurs in by creating an inverted index, consisting of a dictionary and postings.

    docID = within a document collection, we assume that each document has a unique serial number
    """
    def __init__(self, ldocs):
        self.dict_docs_terms = self.tokenizer(ldocs)
        lterms = self.preprocess()
        self.invertedList = self.index(lterms)



    def tokenizer(self, ldocs):
        """
        return a dictionary where keys are the docID and value the list of terms occurs in the doc
        :param ldocs:
        :return:
        """
        """
        :param ldocs:
        :return:
        """
        dict_docs_terms =  {}
        for numDoc in range(len(ldocs)):
            lterms = ldocs[numDoc].split(" ")   # term is equal to a word
            dict_docs_terms[numDoc] = lterms
        return dict_docs_terms

    def preprocess(self):
        """
        In this cse preprocess doesn't do anuthing beacause each word is a term.
        :return: a list of all terms appear in all the documents.
        """
        set_terms = set()
        for docID, lterms in self.dict_docs_terms.iteritems():
            for term in lterms:
                set_terms.add(term)
        return list(set_terms)


    def index(self, lterms):
        inverted_list = {k: [] for k in lterms}
        for term in lterms:
            for docID, doc_terms in self.dict_docs_terms.iteritems():
                if term in doc_terms and docID not in inverted_list[term]:
                    inverted_list[term].append(docID)
        return inverted_list

    def intersect(self, termA, termB):
        """
        Executes a conjunctive boolean query (AND) with two terms.
        :param termA: first term to be found.
        :param termB: second term to be found.
        :return: list of docID where term1 AND term2 occur.
        """
        ldocA = sorted(self.invertedList[termA])
        ldocB = sorted(self.invertedList[termB])
        pA = 0
        pB = 0
        solution = []
        while pA < len(ldocA) and pB < len(ldocB):
            if ldocA[pA] == ldocB[pB]:
                solution.append(ldocA[pA])
                pA += 1
                pB += 1
            else:
                if ldocA[pA] < ldocB[pB]:
                    pA += + 1
                else:
                    pB += 1
        return solution

    def intersec_not(self, termA, termB):
        """
        Intersec two terms return the list of Documents wher occur termA AND NOT termB
        :param termA:
        :param termB:
        :return: list of documents
        """

        ldocA = sorted(self.invertedList[termA])
        ldocB = sorted(self.invertedList[termB])
        pA = 0
        pB = 0
        solution = []
        while pA < len(ldocA) and pB < len(ldocB):
            if ldocA[pA] == ldocB[pB]:
                pA += 1
                pB += 1
                if pB >= len(ldocB) and pA < len(ldocA):
                    solution.append(ldocA[pA])
            else:
                if ldocA[pA] < ldocB[pB]:
                    solution.append(ldocA[pA])
                    pA += 1
                else:
                    pB += 1
        return solution



    def __str__(self):
        return str(self.invertedList).strip('[]')





doc0 = "new home sales top forecasts"
doc1 = "home sales rise in july"
doc2 = "increase in home sales in july"
doc3 = "july new home sales rise"
docs = [doc0, doc1, doc2, doc3]

p = InvertedIndex(docs)

#print(p.intersect('home','july'))

print(p.intersec_not('rise','in'))