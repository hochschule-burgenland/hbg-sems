class Document:

    def __init__(self, id:int, title:str, text:str):
        self.id=id
        self.title=title
        self.text=text

class DocumentIndex:

    def __init__(self):
        pass

    def add_to_index(doc:Document) -> None:
        pass

    def find_token(token:str) -> list[Document]:
        pass

class QueryProcessor:

    def __init__(self, index:DocumentIndex):
        self.index=index

    def query(query:str) -> list[Document]:    
        pass

if __name__ == "__main__":

    index= DocumentIndex()
    query_processor= QueryProcessor(index)
    print ("search not implemented yet")