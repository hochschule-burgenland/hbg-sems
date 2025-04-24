from sentence_transformers import CrossEncoder

def initialize_data(documents:list[str], questions:list[dict]) -> None:
    from csv import DictReader
    doc_lines= [
    "id;title;text",
    "1;Oldest Known Song; The oldest known song is the Hurrian Hymn No. 6, which dates back to around 1400 BCE.",
    "2;Bohemian Rhapsody; The iconic song Bohemian Rhapsody, released in 1975, is known for its unique structure and lack of a traditional chorus.",
    "3;Mozart's Early Start; Wolfgang Amadeus Mozart composed his first piece of music at the age of five.",
    "4;Eye of the Tiger; The iconic rock song Eye of the Tiger is known for its motivational lyrics and driving rhythm.",
    "5;Music and the Brain; Listening to music can stimulate the brain and improve memory, mood, and cognitive function.",
    "6;Universal Language; Music is often referred to as a universal language because it can convey emotions and stories without words.",
    "7;Largest Orchestra; The largest orchestra ever assembled consisted of 8,097 musicians and performed in Frankfurt, Germany, in 2019.",
    "8;Music Therapy; Music therapy is used to help patients with various conditions, including depression, anxiety, and chronic pain.",
    "9;Birds and Music; Some birds, like the lyrebird, can mimic musical instruments and human-made sounds.",
    "10;Quintet; A team of five people can form a band and create music as a quintet."
    ]
    documents.extend(list(DictReader(doc_lines, delimiter=';', skipinitialspace=True)))

    question_lines =[
    "question;doc;method",
    "what are very old songs;1;keyword-search",
    "what was the first vocal ever sung;1;synonyms",
    "can animals make music;9;meronyms",
    "what was the first song;1;word-vector-search",
    "can music bring me back to an active life;8;passage-retrieval",
    "can a five years old make music;3;passage-retrieval",
    "is there music about animals;4;passage-retrieval",    
    ]
    questions.extend(list(DictReader(question_lines, delimiter=';', skipinitialspace=True)))
   
class Score:

    def __init__(self, question:str, document:str, score:float):
        self.question=question
        self.document=document
        self.score=score

    def __repr__(self):
        return f"  score:{self.score} text={self.document}"

model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L6-v2')

if __name__ == "__main__":
    _s=[]
    _q=[]
    initialize_data(_s,_q)
    sentences=[d["text"] for d in _s]
    questions=[q["question"] for q in _q]
    for q in questions:
        print ("scoring ...")
        scores=[]
        for s in sentences:
            score= model.predict([q+" ?",s])
            scores.append(Score(q,s,score))
        scores.sort(key=lambda s: s.score, reverse=True)
        print(q)
        for s in scores[:3]: 
            print(s)    
