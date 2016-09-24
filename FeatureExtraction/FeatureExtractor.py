from PreProcess import doPreProcessing
from VectorSpaceModel import convertToVSM
from TF_ISF import calcMeanTF_ISF

# Feature Vector -
# Features - [ Mean_TF_ISF, Sentence Length,  Sentence Position    ....           ]
# Indexes  - [     0      ,        1       ,          2        ,   ....           ]

def extractFeatures(ip_doc):
	ip_file = open(ip_doc)
	ip_doc = ip_file.read()
	ip_file.close()
	sentences, lengths = doPreProcessing(ip_doc)
	sentences_len = len(sentences)
	maxlen = max(lengths)
	VSM = convertToVSM(sentences)
	featureVectors = []
	for i in range(sentences_len):
		fVect = []
		fVect.append(calcMeanTF_ISF(VSM,i))
		fVect.append(lengths[i]*1.0/maxlen)
		if i <= sentences_len/2:
			fVect.append(0.9 - 1.6*i/sentences_len)
		else:
			fVect.append(0.1 + 1.6*(min([i-sentences_len/2, sentences_len/2]))/sentences_len)
		featureVectors.append(fVect)	
	print featureVectors