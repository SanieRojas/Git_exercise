
import gensim.downloader as api

def load_word2vec_model():
    print("Succesful process initiation...")
    model = api.load('word2vec-google-news-300')
    print("Model Word2Vec succesfully loaded")
    return model

def get_word_list(model):
    words_list = list(model.index_to_key)
    print("Words listed successfully for analysis")
    return words_list

if __name__ == "__main__":
    model = load_word2vec_model()
    words_list = get_word_list(model)