def calcMeanTF_ISF(VSM, index):
	vocab_len = len(VSM[index])
	sentences_len = len(VSM)
	count = 0
	tfisf = 0
	for i in range(vocab_len):
		tf = VSM[index][i]
		if(tf>0):
			count += 1
			sent_freq = 0
			for j in range(sentences_len):
				if(VSM[j][i]>0): sent_freq += 1
			tfisf += (tf)*(1.0/sent_freq)	
	if(count > 0):
		mean_tfisf = tfisf/count
	else:
		mean_tfisf = 0
	return mean_tfisf 
