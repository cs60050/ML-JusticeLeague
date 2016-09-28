from nltk.corpus   import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer

def doPreProcessing(ip_doc,count):
    ss = SnowballStemmer("english")
    fulldocwithoutStemming = []
    fulldoc = []
    smallsumm = []
    largesumm = []
    sentences = ip_doc.split('\n')
    for sent in sentences:
        tokens =  word_tokenize(sent)
        words = tokens
        words = list(filter(lambda x: x != "'" and\
                                      x != "`" and\
                                      x != "." and\
                                      x != "," and\
                                      x != "-"\
                                      , words))
        if tokens:
            fulldocwithoutStemming.append([str(word) for word in words][1:])
        words = [w.lower() for w in words]
        words = [str(ss.stem(word)) for word in words if word not in stopwords.words('english')]
        if words:
            fulldoc.append(words[1:])
            if(words[0]=="1"):
                smallsumm.append(words[1:])
                largesumm.append(words[1:])
            elif(words[0]=="2"):
                largesumm.append(words[1:])
    return smallsumm,largesumm,fulldoc,fulldocwithoutStemming
