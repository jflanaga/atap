from readers import HTMLCorpusReader  # to read html corpus
from preprocess import Preprocessor  # to transform html to pickle

from src.paths import RAW_CORPUS, INTERIM_CORPUS

corpus = HTMLCorpusReader(RAW_CORPUS)
preprocessor = Preprocessor(corpus, INTERIM_CORPUS)
preprocessor.transform()
