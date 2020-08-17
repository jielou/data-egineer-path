# Intro to Natural Language Processing

## Key concepts

### Tokenization
- turn a string or doc into tokens
- one step in preparing a text for NLP
- Examples:
    - breaking out words or sentences
    - separating punctuation
- common libraryß
    - nltk: natural language toolkit

### bag of words
- basic method for finding topics in a text
- first create tokens using tokenization and then count up all the tokens
- the more frequent a word, the more important it might be

### preprocess

- tokenization to create a bag of words
- lowercasing words
- lemmatization/stemming: shorten words to their root stems
- removing stopwords, punctuation, or unwanted tokens

### tf-idf

- term frequency - inverse document frequency
- determine the most important words in each document
- formula: Wi,j = tfi,j*log(N/dfi)
    - Wi,j = tf-idf weight for token i in document j
    - tfi,j = number of occurences of token i in document j (percentage share of the word compared to all tokens in the document)
    - dfi = number of documents that contain token i
    - N = total number of documents

### Named Entity Recognition

NLP task to identify important named entities in the text
- people, places, organizations
- dates, states, works of art
- .. and other categories




    

