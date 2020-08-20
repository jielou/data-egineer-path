# intro to NLP Feature Engineering

## key concepts

### readability tests

#### Flesch reading ease
- one of the oldest and most widely used tests
- dependent on two factos:
    - greater the average sentence lenght, harder the text is to read
    - greater the average number of syllables in a word, harder the text is to read
- higher the score, greater the readability

#### Gunning fog index
- also dependent on average sentence lenght
- greater the percentage of complex words, harder the text is to read
- higher the index, lesser the readability

#### python
use textatistic library

### tokenization and lemmatization

#### text preprocessing techniques
- convert words into lowercase
- remove leading and trailing whitespaces
- remove punctuation
- remove stopwords
- expand contractions
- remove special characters(numbers, emojis, etc.): `isalpha()`

#### tokenization
- use spacy library

#### lemmatization
- convert word into its base form
- use spacy library

### Part of speech tagging

#### applications
- word-sense disambiguation
- sentiment analysis
- question answering
- fake news and opinion spam detection

#### definitions
assigning every word, its corresponding part of speech

Example: `Jane is an amzing quitarist`
- Jane: proper noun
- is: verb
- an: determiner
- amzing: adjective
- quitarist: noun

### Named entity recognition
- identifying and classifying named entities into predefined categories
- categories include person, organization, country, etc.

## a bag of words
count of words

## n-grams
contiguous sequence of n elements (or words) in a given document
- short comings: curse of dimensionality

## consine score
- value bettween -1 and 1
- in NLP, value between 0 and 1
- Robust to document length