from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer

words = ['table', 'probably', 'wolves', 'playing', 'is', 'dog', 'the', 'beaches', 'ground', 'dreamt', 'envision']
stermmer = ['PORTER', 'LANCASTER', 'SNOWBALL']

stermmer_porter = PorterStemmer()
stermmer_lancaster = LancasterStemmer()
stermmer_snowball = SnowballStemmer('english')

formatted_row = '{:>16}'*(len(stermmer) + 1)
print "\n", formatted_row.format('WORD', *stermmer), "\n"
for word in words:
	stemmed_words = [stermmer_porter.stem(word), stermmer_lancaster.stem(word), stermmer_snowball.stem(word)]
	print formatted_row.format(word, *stemmed_words)	