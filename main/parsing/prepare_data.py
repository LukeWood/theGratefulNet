import nltk
import itertools
import numpy as np

class data_manager:
    def __init__(self,vocab_size=8000):
        self.vocabulary_size = vocab_size
        self.unknown_token = "UNKNOWN_TOKEN"
        self.sentence_start_token = "SENTENCE_START"
        self.sentence_end_token = "SENTENCE_END"
        self.sentences = []
        self.parsed_sentences = []

    def add_data(self,f0):
        self.sentences = self.sentences + self.__tokenize(["%s %s %s" % (self.sentence_start_token, x, self.sentence_end_token) for x in open(f0,"r")])
        self.__remove_uncommon()

    def __tokenize(self,sentences):
        return [nltk.word_tokenize(sentence) for sentence in sentences]

    #Only call this after we load all data
    def __remove_uncommon(self):
        word_freq = nltk.FreqDist(itertools.chain(*self.sentences))
        words = word_freq.most_common(self.vocabulary_size-1)
        self.index_to_word= [x[0] for x in words]
        self.index_to_word.append(self.unknown_token)
        self.word_to_index = dict([(w,i) for i,w in enumerate(self.index_to_word)])
        self.parsed_sentences = []
        for i,sent in enumerate(self.sentences):
            self.parsed_sentences.append([w if w in self.word_to_index else self.unknown_token for w in sent])

    def convert_to_words(self,x):
        return [self.index_to_word[y] for y in x]

    def get_raw_data(self):
        return self.parsed_sentences

    def get_training_data(self):
        X = np.asarray([[self.word_to_index[w] for w in sent[:-1]] for sent in self.parsed_sentences])
        Y = np.asarray([[self.word_to_index[w] for w in sent[1:]] for sent in self.parsed_sentences])
        return X, Y

    def get_indices(self):
        return self.word_to_index, self.index_to_word
