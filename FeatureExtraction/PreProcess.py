from nltk.corpus   import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
import nltk.data
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

def doPreProcessing(ip_doc):
	ss = SnowballStemmer("english")
	fulldoc = []
	lengths = []
	sentencesList = []
	sentencesWithoutStemming = tokenizer.tokenize(ip_doc)
	sentencesWithoutStemming = filter(lambda a: a.strip() != ".", sentencesWithoutStemming)
	for sent in sentencesWithoutStemming:
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
									  
			words = [str(ss.stem(word)) for word in words if word not in stopwords.words('english')]	
			length = len(words)	

			fulldoc.append(words)
			lengths.append(length)
	for sent in sentencesWithoutStemming:
		if(sent!="."):
			sentencesList.append(sent)

	return fulldoc, lengths, sentencesList
