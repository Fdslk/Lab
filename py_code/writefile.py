import os
import sys

myword = ['a', 'b', 'c', 'd']
max_index = len(myword)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(myword)):
	if index_value < (max_index - 1):
		filewriter.write(myword[index_value] + '\t')
	else:
		filewriter.write(myword[index_value] + '\t')
filewriter.close()
print "Output written to file"
