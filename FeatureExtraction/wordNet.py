from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk import pos_tag
import operator, heapq
import sys, re 
import nltk.data
#from PreProcess import doPreProcessing

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

reload(sys)  
sys.setdefaultencoding('utf8')


def doPreProcessing(ip_doc):
	fulldoc = []
	#lengths = []
	#sentences1 = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', ip_doc)
	sentences = tokenizer.tokenize(ip_doc)
	sentences = filter(lambda a: a.strip() != ".", sentences)
			
	#sentences2 = ip_doc.split("\n")
	#print len(sentences), len(sentences1), len(sentences2)
	for sent in sentences:
		if(sent != "."):
			tokens =  word_tokenize(sent)
			#words = [w.lower() for w in tokens]
			words = [w for w in tokens]
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
									  
			words = [str(word) for word in words if word not in stopwords.words('english')]	
			length = len(words)	
			fulldoc.append(words)
			#lengths.append(length)
	return fulldoc, sentences




def wordNetFeature(ip_doc):
	ip_file = open(ip_doc)
	ip_doc = ip_file.read()
	ip_file.close()
	sentences, sent_exact = doPreProcessing(ip_doc)
	sentences_len = len(sentences)
	#print sent_exact
	#maxlen = max(lengths)	
	dic={}
	keywords=[]
	for i in sentences:
		wordpos = pos_tag(i)
		#print wordpos
		for j in xrange(0,len(i)):	
			if wordpos[j][1]=="NNP":
				keywords.append(wordpos[j][0])
			elif wordpos[j][1].startswith("NN") or wordpos[j][1].startswith("JJ"):
				keywords.append(wordpos[j][0].lower())		
	keywords=list(set(keywords))
					
	for i in sentences:
		for j in xrange(0,len(i)):	
			word=i[j]
			li=wordnet.synsets(word)
			for k in li:
				if k not in dic:
					dic[k]=1
					#dic[k]=[word]
				else:
					dic[k]+=1
					#dic[k].append(word)
	dic = sorted(dic.items(), reverse=True, key=operator.itemgetter(1))				
	for i in xrange(0,len(dic)):
		if dic[i][1]==1:
			break
	dic=dic[:i]		
	keywords_tuple=[]
	for i in xrange(0,len(keywords)):
		if keywords[i][0].isupper():
			keywords_tuple.append([keywords[i],1.0])	
		else:
			keywords_tuple.append([keywords[i],0.0])
	#print len(keywords_tuple), len(dic)	
	for i in xrange(0,len(keywords)):
		if keywords[i][0].islower():
			for j in xrange(0,len(dic)):
				if dic[j][1]==1:
					break
				else:
					try:	
						wordnw = wordnet.synsets(keywords[i])[0]
						temp=wordnw.wup_similarity(dic[j][0])
						if temp>keywords_tuple[i][1]:
							keywords_tuple[i][1]=temp
					except:
						pass		
					
	keywords_tuple = dict(keywords_tuple)
	sent_weight=[0]*sentences_len					
	for i in xrange(0,sentences_len):
		cnt=0
		for j in sentences[i]:
			if j in keywords_tuple:
				sent_weight[i]+=keywords_tuple[j]
				cnt+=1
		if cnt>0:
			sent_weight[i]/=cnt	
	#print sent_weight
	
	return sent_weight
	#sent_req = sorted(list(zip(*heapq.nlargest(3, enumerate(sent_weight), key=operator.itemgetter(1)))[0]))	
	#for i in sent_req:
		#print "".join(sent_exact[i])	
