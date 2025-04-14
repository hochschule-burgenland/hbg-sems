from __future__ import annotations
import cmd
from uuid import UUID, uuid1

class Document:
    
    def __init__(self, id:UUID, text:str):        
        self.text=text
        self.id=id

    def __str__(self):
        return f"doc[id={self.id}, text={self.text}]"

class DocumentStore:

    def __init__(self):
        self.documents=[]

    def get_document(self,id:any) -> Document:
        for doc in self.documents:
            if doc.id==id:
                return doc
        return None    

class DocumentIndex:
    
    def __init__(self):
        self.entries={}       

    def add_entry(self, key:str, doc_id:any) -> None:
        self.entries.setdefault(key,set())
        self.entries[key].add(doc_id)    

    def search(self,term:str) -> list[any]:
        if self.entries.__contains__(term):
            return self.entries[term]     
        else:
            return []

class DocumentProcessor:

    def __init__(self, store:DocumentStore, index:DocumentIndex):
        self.store=store
        self.index=index
    
    def ingest(self,str:str) -> None:
        doc=Document(uuid1(), str)
        self.store.documents.append(doc)
        tokens= str.split()
        for tok in tokens:
            self.index.add_entry(tok,doc.id)

class QueryProcessor:
     
    def __init__(self, store:DocumentStore, index:DocumentIndex):
        self.store=store
        self.index=index

    def search(self, query:str) -> list[Document]:
        result=set()
        tokens= query.split()
        for tok in tokens:
            ids= self.index.search(tok)
            result.update([self.store.get_document(id) for id in ids])
        return result

class SearchEngine:

    def __init__(self):
        self.store= DocumentStore()    
        self.index= DocumentIndex()    
        self.doc_processor= DocumentProcessor(self.store,self.index)
        self.query_processor= QueryProcessor(self.store,self.index)

    def ingest(self,text:str) -> None:
        self.doc_processor.ingest(text)

    def search(self, text:str) -> list[str]:
        docs= self.query_processor.search(text)
        return [doc.text for doc in docs]

if __name__ == "__main__":
    
    search_engine=SearchEngine()
    
    with open("simple_search/documents.txt","r",encoding="utf-8") as f:
        lines= f.read().splitlines()    
    for line in lines:
        search_engine.ingest(line)

    query=input("Suchbegriff (oder exit): ")
    while query !="exit":
        docs= search_engine.search(query)
        for doc in docs:
            print(doc)            
        query= input("Suchbegriff (oder exit): ")




