from nltk.corpus   import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

def doPreProcessing(ip_doc,ip_docWithoutStemming):
	ss = SnowballStemmer("english")
	fulldoc = []
	lengths = []
	sentencesList = []
	sentences = ip_doc.split("\n")
	sentencesWithoutStemming = ip_docWithoutStemming.split("\n")
	for sent in sentences:
		if(sent != "."):
			tokens =  word_tokenize(sent)
			words = [w.lower() for w in tokens]
			words = list(filter(lambda x: x != "'" and\
										  x != "`" and\
										  x != "." and\
										  x != "," and\
										  x != "-" and\
										  x != "?" and\
										  x != ":" and\
										  x != "!" and\
										  x != ";"\
										  , words))
			words = [str(ss.stem(word)) for word in words if word not in stopwords.words('english')]
			length = len(words)
			fulldoc.append(words)
			lengths.append(length)
	for sent in sentencesWithoutStemming:
		if(sent!="."):
			sentencesList.append(sent)

	return fulldoc, lengths, sentencesList
