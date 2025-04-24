from sentence_transformers import SentenceTransformer, util
import numpy as np
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

documents= [
    "It's considerably warmer than the mediterranean climate",   
    "In summer, it gets quite hot, and that's also due to the exhaust fumes",
    "The level of harmful emissions is alarming",
    "Industry spews a lot of acidic sulfur into the air",
    "the temperature there is quite high"
]
questions=["is it warm"]

def search_and_print(q_vector, doc_vectors):
    scores=util.semantic_search(q_vector,doc_vectors,top_k=3)
    result= []
    for score in scores:
            for s in score:
                index=s['corpus_id']
                print (f"  {round(s['score'],2)} {documents[index]}")
                result.append(documents[index])
    return result

if __name__ == "__main__":
    doc_vectors=model.encode(documents)
    for q in questions:
        q_vector=model.encode(q)
        print(f"query: {q} \nfirst pass:")
        res1=search_and_print(q_vector,doc_vectors)
        res1_vectors=[model.encode(s) for s in res1]
        mean_vector= np.mean(res1_vectors, axis=0)
        print(f"second pass:")
        search_and_print(mean_vector,doc_vectors)


    
        
        
        


