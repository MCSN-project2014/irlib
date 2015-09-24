__author__ = 'dido-ubuntu'
import unittest

from irlib.boolean_retrieval import BooleanRetrieval

class TestBooleanQueries(unittest.TestCase):

    def setUp(self):
        # esercizio 1.1 pag 9 libro
        self.doc0 = "new home sales top forecasts"
        self.doc1 = "home sales rise in july"
        self.doc2 = "increase in home sales in july"
        self.doc3 = "july new home sales rise"
        self.docs = [self.doc0, self.doc1, self.doc2, self.doc3]
        self.indx = BooleanRetrieval.InvertedIndex(self.docs)



    #def tearDown(self):
     #   self.array_strings = ["abh", "aec", "bbb",  "aah", "ggg", "lbb", "lll"] # esempio  pag 6-3 notes

    def test_intersect(self ):

        self.assertEqual(self.indx.intersect('home', 'july'), [1, 2, 3])
        self.assertEqual(self.indx.intersect('new', 'top'), [0])
        self.assertEqual(self.indx.intersect('home', 'sales'), [0, 1, 2, 3])


    def test_intersect_and_not(self ):

        self.assertEqual(self.indx.intersec_and_not('new', 'top'), [3])
        self.assertEqual(self.indx.intersec_and_not('home', 'sales'), [])
        self.assertEqual(self.indx.intersec_and_not('sales', 'in'), [0, 3])