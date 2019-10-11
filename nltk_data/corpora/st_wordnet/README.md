# nltk_data

Instead of replicating the data here, take the following steps to get the data from its source.

- Install NLTK if you don't have it already (see http://www.nltk.org/install.html)
- Use the default location (~/nltk_data) or point to it with NLTK_DATA
- Install wordnet
- Create directory "st_wordnet" under directory "corpora" in nltk_data
- Go to http://ai.stanford.edu/~rion/swn/
- Under "Sense-clustered Wordnets", copy file WN 2.1 -32065 synsets: senseclusteredWN_-1.5.tgz
- Unzip the file and move the data to the st_wordnet directory

You should have the following files:
- data.adj
- data.adv
- data.noun
- data.verb
- index.adj
- index.adv
- index.noun
- index.sense
- index.verb

In addition, copy the following files from nltk_data/corpora/wordnet to st_wordnet:
- adj.exc
- adv.exc
- lexnames
- noun.exc
- verb.exc

(An issue with the lexnames file arose, which I bypassed with code in st_wordnet.py - see https://groups.google.com/forum/#!topic/nltk-users/AO6EGyPya6s. Still waiting on a response from the author to clean this up).

The data should now be ready to use.
