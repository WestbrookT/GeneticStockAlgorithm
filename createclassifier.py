import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import nltk, pickle

def word_feats(words):
    return dict([(word, True) for word in words])

def prepare(text):
    out = ({word : True for word in text.split()})
    return out


negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

i = 0


negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = int(len(negfeats))
poscutoff = int(len(posfeats))








t = ({'bad': True})

trainfeats = negfeats + posfeats
#testfeats = negfeats[negcutoff:] + posfeats[poscutoff:]
print(negfeats[0])

classifier = NaiveBayesClassifier.train(trainfeats)
print(classifier.classify(prepare('hitler is a hero')))

