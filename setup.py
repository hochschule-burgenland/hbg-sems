from sentence_transformers import SentenceTransformer, util
from gensim.models import KeyedVectors
from huggingface_hub import hf_hub_download
from pathlib import Path
import os

if __name__=="__main__":
    print("setup: check/load model sentence-transformers/all-mpnet-base-v2 (may take some time)")
    model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
    query_embedding = model.encode("How big is London")
    passage_embedding = model.encode([
        "London has 9,787,426 inhabitants at the 2011 census",
        "London is known for its financial district",
    ])
    print("   Similarity:", util.dot_score(query_embedding, passage_embedding))
    print("setup: model OK")

    print("setup: check/load model from file model_cache/enwiki_20180420_100d")
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