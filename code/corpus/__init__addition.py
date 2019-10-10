# Add this snippet near the regular wordnet definition

 st_wordnet = LazyCorpusLoader(
    'st_wordnet',
    WordNetCorpusReader,
    LazyCorpusLoader('st_wordnet', CorpusReader, r'.*/wn-data-.*\.tab', encoding='utf8'),
)
