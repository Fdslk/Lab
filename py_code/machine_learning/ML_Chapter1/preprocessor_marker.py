from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
input_classes = ['adui', 'ford', 'adui', 'toyota', 'ford', 'bmw']
label_encoder.fit(input_classes)
index = []
print "\nClass mapping:"
for i, item in enumerate(label_encoder.classes_):
	index.append(i)
	print item, '-->', i
	
labels = ['toyota', 'adui', 'ford']
New_labels = []
for label in labels:
	if label in input_classes:
		New_labels.append(label)
encoded_labels = label_encoder.transform(New_labels)
print "\nLabels =", New_labels
print "Encode labels =", list(encoded_labels)

encoded_labels = [2, 1, 0, 3, 1]
labels = []
for encoded_label in encoded_labels:
	if encoded_label in index:
		labels.append(encoded_label)
decoded_labels = label_encoder.inverse_transform(labels)
print "\nEncoded labels = ", encoded_labels
print "Decoded labels = ", list(decoded_labels)
