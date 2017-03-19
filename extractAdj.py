import nltk
#nltk.download() 
import re
import simplejson as json
from nltk import word_tokenize, pos_tag
from collections import Counter
from collections import OrderedDict
f=open('text1.txt','rU')
raw=f.read()
tokens = nltk.word_tokenize(raw)
adj=nltk.pos_tag(tokens) == 'JJ'
#text = nltk.Text(adj.lower() for adj in nltk.corpus.brown.words())
#print(text.similar('charming'))
adj = [token for token, pos in pos_tag(word_tokenize(raw)) if pos.startswith('JJ')]
counts = Counter(adj)
countorderedm = OrderedDict(sorted(counts.items(), key=lambda t: t[1], reverse=True)).keys()
common_words = frozenset(("new", "old", "good", "more", "better", "best", "great", "much", "big", "own", "most", "first", "many", "large", "bigger", "Spanish"))
#print(countorderedm)
with open("trial1.txt", "w") as f:
    for key in countorderedm:
        if (key not in common_words):
            print(key, file=f)
#print (sorted(counts, key=counts.__getitem__))
#print(adj)
