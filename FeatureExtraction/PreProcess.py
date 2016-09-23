from nltk.corpus   import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

def doPreProcessing(ip_doc):
	ps = PorterStemmer()
	fulldoc = []
	lengths = []
	sentences = sent_tokenize(ip_doc)
	for sent in sentences:
		if(sent != "."):
			tokens =  word_tokenize(sent)
			words = [w.lower() for w in tokens]
			words = list(filter(lambda x: "'" not in x and\
										  "`" not in x and\
										  "." not in x and\
										  "," not in x and\
										  "-" not in x and\
										  "?" not in x and\
										  ":" not in x and\
										  "!" not in x and\
										  ";" not in x\
										  , words))
			length = len(words)	
			words = [str(ps.stem(word)) for word in words if word not in stopwords.words('english')]	
			fulldoc.append(words)
			lengths.append(length)
	return fulldoc, lengths
