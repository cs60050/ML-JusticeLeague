from nltk.corpus   import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

def doPreProcessing(ip_doc):
	ps = PorterStemmer()
	fulldoc = []
	smallsumm = []
	largesumm = []
	sentences = sent_tokenize(ip_doc)
	for sent in sentences:
		tokens =  word_tokenize(sent)
		words = [w.lower() for w in tokens]
		words = list(filter(lambda x: "'" not in x and\
									  "`" not in x and\
									  "." not in x and\
									  "," not in x and\
									  "-" not in x\
									  , words))	
		words = [str(ps.stem(word)) for word in words if word not in stopwords.words('english')]	
		fulldoc.append(words[1:])
		if(words[0]=="1"):
			smallsumm.append(words[1:])
			largesumm.append(words[1:])
		elif(words[0]=="2"):
			largesumm.append(words[1:])
	return smallsumm,largesumm,fulldoc
