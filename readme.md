## Installation der erforderlichen Libraries und Modelle
Führen sie folgende Schritte durch
- `conda create -n sems`
- `conda activate sems`
- `conda install flask, conda-forge::sentence-transformers=0.30.0, transformers, gensim, huggingface_hub`
- `conda install conda-forge::python-annoy, nltk`
- `python setup.py`
  

## Ergebnis: Speicherort der geladenen Modelle
- `%USERPROFILE%/.cache/huggingface/hub`
- `c:\nltk_data,  /usr/local/share/nltk_data` 
- `./model_cache`