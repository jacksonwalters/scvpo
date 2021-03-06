import os, math
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse
from load_scotus_data import scotus_opinion_data

#output paths
DATA_PATH = ".\\data\\tf-idf\\scotus_opinion\\"
TFIDF_MATRIX_PATH = os.path.join(DATA_PATH,'tfidf_matrix.npz') #tf-idf matrix filepath
TFIDF_ROWS_PATH = os.path.join(DATA_PATH,"tfidf_rows.csv") #opin ids filepath
TFIDF_COLS_PATH = os.path.join(DATA_PATH,"tfidf_cols.csv") #vocab filepath

#perform a TF-IDF analysis on corpus of opinion text data
def tfidf_opins():
    #store opinion data as dataframe
    opin_df = scotus_opinion_data()

    #generate corpus
    corpus=[]
    for opin in list(opin_df['opinion']):
        try:
            if math.isnan(opin):
                corpus.append("")
        except TypeError:
            opin_text = str(opin)
            corpus.append(opin_text)

    #generate tfidf matrix. set maximum document freq. and minimum cut-off to limit dumb non-words
    max_n=1 #specify maximum n-gram size (length of phrases)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1,max_n), stop_words="english", min_df=.00001,max_df=.30)

    #matrix with each row corresponding to an opinion
    #and each column an n-gram with n specified above
    print(f"Building TF-IDF matrix with {max_n}-grams ...")
    tfidf_matrix =  tf.fit_transform(corpus)
    print("Finished TF-IDF matrix with shape",tfidf_matrix.shape)
    #write sparse tdidf matrix to compressed .npz file
    scipy.sparse.save_npz(TFIDF_MATRIX_PATH, tfidf_matrix)
    print("Saved sparse matrix to ",TFIDF_MATRIX_PATH)

    #mapping {column index : feature name}
    vocab = tf.get_feature_names()
    #mapping {row index : opinion id}
    #opinion_id = U.S. Cite | lower-case-v-name-abbreviated
    citation = list(map(str,opin_df['citation']))
    name = list(map(str,opin_df['case_name']))
    opin_id = ["|".join([citation[i],name[i]]) for i in range(tfidf_matrix.shape[0])]
    #store index mappings as CSV
    pd.DataFrame(opin_id).to_csv(TFIDF_ROWS_PATH, encoding='utf-8',index=False)
    print("Saved rows of TF-IDF matrix to ",TFIDF_ROWS_PATH)
    pd.DataFrame(vocab).to_csv(TFIDF_COLS_PATH, encoding='utf-8',index=False)
    print("Saved cols of TF-IDF matrix to ",TFIDF_COLS_PATH)

if __name__ == "__main__":
    tfidf_opins()
