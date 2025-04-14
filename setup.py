print("setup: starting imports (may take some time)")
from sentence_transformers import SentenceTransformer, util
from gensim.models import KeyedVectors
from huggingface_hub import hf_hub_download
from pathlib import Path
import os

if __name__=="__main__":
    print("setup: check/load model sentence-transformers/all-mpnet-base-v2 (may tak some time and strange messages)")
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    query_embedding = model.encode("How big is London")
    passage_embedding = model.encode([
        "London has 9,787,426 inhabitants at the 2011 census",
        "London is known for its financial district",
    ])
    print("   Similarity:", util.dot_score(query_embedding, passage_embedding))
    print("setup: model OK")

    print("setup: check/load model sentence-transformers/msmarco-bert-base-dot-v5  (may take some time and strange messages)")
    model = SentenceTransformer("sentence-transformers/msmarco-bert-base-dot-v5")
    query_embedding = model.encode("How big is London")
    passage_embedding = model.encode([
        "London has 9,787,426 inhabitants at the 2011 census",
        "London is known for its financial district",
    ])
    print("   Similarity:", util.dot_score(query_embedding, passage_embedding))
    print("setup: model OK")


    print("setup: check/load model enwiki_20180420_100d (may take some time and strange messages)")
    model_filename="enwiki_20180420_100d"
    proj_dir=f"{os.getcwd()}"
    local_cache_dir=f"{proj_dir}/model_cache/"

    if not Path(f"{local_cache_dir}/{model_filename}.bin").exists(): 
        model = KeyedVectors.load_word2vec_format(hf_hub_download(repo_id="Word2vec/wikipedia2vec_enwiki_20180420_100d", 
                    local_dir=local_cache_dir, filename=f"{model_filename}.txt"))
        with open(f"{local_cache_dir}/{model_filename}.bin","wb") as f:
            model.save(f)
    else:
        model = model=KeyedVectors.load(f"{local_cache_dir}/{model_filename}.bin")
    print("setup: model OK")

    print("setup: check/load model deepset/minilm-uncased-squad2 (may take some time and strange messages)")
    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
    model_name = "deepset/minilm-uncased-squad2"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': 'Why is model conversion important?',
        'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
    }
    res = nlp(QA_input)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("setup: model OK")

    from sentence_transformers import CrossEncoder
    print("setup: check/load model cross-encoder/ms-marco-MiniLM-L6-v2 (may take some time and strange messages)")
    model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L6-v2')
    scores = model.predict([
        ("How many people live in Berlin?", "Berlin had a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers."),
        ("How many people live in Berlin?", "Berlin is well known for its museums."),
    ])
    print("setup: model OK")