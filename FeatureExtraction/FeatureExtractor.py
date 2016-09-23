from PreProcess import doPreProcessing
from VectorSpaceModel import convertToVSM
from TF_ISF import calcMeanTF_ISF

# Feature Vector -
# Features - [ Mean_TF_ISF, Sentence Length,    ....           ]
# Indexes  - [     0      ,        1       ,    ....           ]

def extractFeatures(ip_doc):
	ip_file = open("./1_fulldoc.txt")
	ip_doc = ip_file.read()
	ip_file.close()
	sentences, lengths = doPreProcessing(ip_doc)
	maxlen = max(lengths)
	VSM = convertToVSM(sentences)
	featureVectors = []
	for i in range(len(sentences)):
		fVect = []
		fVect.append(calcMeanTF_ISF(VSM,i))
		fVect.append(lengths[i]*1.0/maxlen)
		featureVectors.append(fVect)	
	print featureVectors