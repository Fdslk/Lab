from computer_word_vector import select_feature
import sys

input_file = sys.argv[1]
sf = select_feature()
data = sf.count_Words(input_file)
print len(data)