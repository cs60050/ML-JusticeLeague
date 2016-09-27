def convertToVSM(sentences):
	vocabulary = []
	for sent in sentences:
		vocabulary.extend(sent)
	vocabulary = list(set(vocabulary))
	vectors = []
	for sent in sentences:
		vector = []
		for token in vocabulary:
			vector.append(sent.count(token))
		vectors.append(vector)
	return vectors


