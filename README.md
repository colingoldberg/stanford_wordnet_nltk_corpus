# stanford_wordnet_nltk_corpus
Based on the Stanford WordNet Project - to reduce granularity of WordNet synsets to a more manageable number

## Motivation for this project
- There are many examples where synset differences are too fine-grained
- This makes it more difficult to select a context for a given word

See https://github.com/nltk/nltk/wiki/Adding-a-Corpus for details. I did not go to the extent of creating a pull request for this corpus (partly in view of the lexnames issue (see https://github.com/colingoldberg/stanford_wordnet_nltk_corpus/tree/master/nltk_data/corpora/st_wordnet).

## A simple test
```
from nltk.corpus import st_wordnet as wn
word = 'large'
synsets = wn.synsets(word)
```
