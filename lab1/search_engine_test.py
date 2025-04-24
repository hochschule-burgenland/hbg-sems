import unittest
from search_engine import QueryProcessor 
from search_engine import lemmatize_tokens

class SearchEngineTest(unittest.TestCase):

    def testFindSimilarTokens(self):
        qp= QueryProcessor(None)
        result= qp.find_similar_tokens("earliest")      
        self.assertTrue("old" in result)          