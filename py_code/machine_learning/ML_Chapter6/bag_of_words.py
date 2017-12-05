import numpy as np
from nltk.corpus import brown
from chunking import splitter
from sklearn.feature_extration.text import CountVectorizer
if __name_ == '__main__':
	data = ' '.join(brown.words()[:10000])
	num_words = 2000
	chunks = []
	counter = 0
	text_chunks = splitter(data, num_words)
	for text in text_chunks:
		chunk = {'index':counter, 'text':text}
		chunks.append(chunk)
		counter += 1
	vectorizer = CountVectorizer(min_df=5, max_df=.95)
	doc_term_matrix = vectorizer.fit_transform([chunk['text'] for chunk in chunks])
	vocab = np.array(vectorizer.get_feature_names())
	print "\nVocabulary:"
	print vocab
	print "\nDocument term matrix:"
	chunk_names = ['chunk-0', 'chunk-1', 'chunk-2', 'chunk-3', 'chunk-4']
	formatted_row = '{:>12}'*(len(chunk_names)+1)
	print '\n', formatted_row.format('Word', *chunk_names), '\n'
	
	for word, item in zip(vocab, doc_term_matrix.T):
		output = [str(x) for x in item.data]
		print formatted_row.format(word, *output)