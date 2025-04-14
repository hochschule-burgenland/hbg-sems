import unittest
from simple_searchengine import Document, DocumentStore, DocumentIndex,DocumentProcessor, QueryProcessor
from uuid import uuid1

class SearchEngineTest(unittest.TestCase):

    line1="wach auf"
    line2="ich wach "
    
    def test_documentindex(self):
        idx=DocumentIndex()
        idx.add_entry("wach",0)
        idx.add_entry("auf",0)
        idx.add_entry("ich",1)
        idx.add_entry("wach",2)
        
        ids=idx.search("wach")
        self.assertEqual(len(ids),2)
        
    def test_documentstore(self):    
        ds=DocumentStore()
        id=uuid1()
        doc=Document(id,SearchEngineTest.line1)
        ds.documents.append(doc)
        self.assertEqual(ds.get_document(id), doc)
        self.assertEqual(doc.text, SearchEngineTest.line1)

    def test_document_processor(self):
        ds= DocumentStore()
        idx= DocumentIndex()
        a= DocumentProcessor(ds,idx)
        a.ingest(SearchEngineTest.line1)
        a.ingest(SearchEngineTest.line2)

        self.assertEqual(len(ds.documents),2)
        ids= idx.search("wach")
        self.assertEqual(len(ids),2)

    def test_query_processor(self):
        ds= DocumentStore()
        idx= DocumentIndex()
        a= DocumentProcessor(ds,idx)
        a.ingest(SearchEngineTest.line1)
        a.ingest(SearchEngineTest.line2)

        qa=QueryProcessor(ds,idx)
        docs=qa.search("wach")
        self.assertEqual(len(docs),2)
        docs=qa.search("auf")
        self.assertEqual(len(docs),1)
        docs=qa.search("ich wach")
        self.assertEqual(len(docs),2)
        

        



        

