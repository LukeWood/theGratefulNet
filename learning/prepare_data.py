import nltk
import itertools
import numpy as np

class data_manager:
    def __init__(self):
        self.vocabulary_size = 8000
        self.unknown_token = "UNKNOWN_TOKEN"
        self.sentence_start_token = "SENTENCE_START"
        self.sentence_end_token = "SENTENCE_END"
        self.sentences = []
        self.parsed_sentences = []

    def read_data(self,f0):
        self.sentences = self.sentences + self.tokenize(["%s %s %s" % (sentence_start_token, x, sentence_end_token) for i in open(f0,"r")])

    def tokenize(self,sentences):
        return [nltk.word_tokenize(sentence) for sentence in sentences]

    #Only call this after we load all data
    def remove_uncommon(self):
        word_freq = nltk.FreqDist(itertools.chain(*self.sentences))
        words = word_freq.most_common(vocabulary_size-1)
        self.index_to_word= [x[0] for x in vocab]
        self.index_to_word.append(unknown_token)
        self.word_to_index = dict([(w,i) for i,w in enumerate(index_to_word)])

        for i,sent in self.sentences:
            self.parsed_sentences[i] = [w if w in word_to_index else unknown_token for w in sent]

    def fetch_data(self):
        return self.parsed_sentences

    def get_training_data(self):
        X = np.asarray([[word_to_index[w] for w in sent[:-1] for sent in self.parsed_sentences]])
        Y = np.asarray([[word_to_index[w] for w in sent[:-1] for sent in self.parsed_sentences]])
        return X, Y
