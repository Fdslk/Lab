from nltk.stem import WordNetLemmatizer

words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'ground', 'dreamt', 'envision']
stermmer = ['PORTER', 'LANCASTER', 'SNOWBALL']

lemmatizer = ['NOUN LEMMATIZER', 'VERB LEMMATIZER']
lemmatizer_wordnet = WordNetLemmatizer()
formatted_row = '{:>24}' * (len(lemmatizer)+1)
print '\n',formatted_row.format('WORD', *lemmatizer), '\n'
for word in words:
	lemmatizer_word = [lemmatizer_wordnet.lemmatize(word, pos='n'), lemmatizer_wordnet.lemmatize(word, pos='v')]
	print formatted_row.format(word, *lemmatizer_word)