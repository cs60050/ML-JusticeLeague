from __future__ import division
from PreProcess import doPreProcessing
from VectorSpaceModel import convertToVSM
from TF_ISF import calcMeanTF_ISF
from tRank import modifiedSummarizer
from wordNet import wordNetFeature
from nltk import pos_tag

# Feature Vector -
# Features - [ Mean_TF_ISF, Sentence Length,  Sentence Position,   textRank,   ProperNouns ,    Numerical Data,   Wordnet        ]
# Indexes  - [     0      ,        1       ,          2        ,   3       ,   4           ,     5            ,      6        ]

def extractFeatures(ip_doc,ip_docWithoutStemming):
    file_name = ip_doc
    ip_file = open(ip_doc)
    ip_doc = ip_file.read()
    ip_file.close()

    ip_file = open(ip_docWithoutStemming)
    ip_docWithoutStemming = ip_file.read()
    ip_file.close()

    sentences, lengths, sentencesWithoutStemming = doPreProcessing(ip_doc,ip_docWithoutStemming)
    sentences_len = len(sentences)
    maxlen = max(lengths)
    VSM = convertToVSM(sentences)
    VSM_deepCopy=VSM[:]
    summarizer = modifiedSummarizer()
    sentenceRanks=summarizer.summarize(VSM_deepCopy,1,None,"english",False,True)
    wordNetWeights = wordNetFeature(file_name)
    featureVectors = []
    for i in range(sentences_len):
        if lengths[i] != 0:     
            fVect = []

            #TF-ISF
            fVect.append(calcMeanTF_ISF(VSM, i))

            #Sentence Length
            fVect.append(lengths[i]*1.0/maxlen)

            #Sentence Position
            if i <= sentences_len/2:
                fVect.append(0.9 - 1.6*i/sentences_len)
            else:
                fVect.append(0.1 + 1.6*(min([i-sentences_len/2, sentences_len/2]))/sentences_len)

            #textRank
            fVect.append(sentenceRanks[i])

            #Proper nouns
            tagged_sent = pos_tag(sentencesWithoutStemming[i].split())
            if len(tagged_sent) != 0:
                fVect.append(len([word for word, tag in tagged_sent if tag == "NNP"])/len(tagged_sent))
            else:
                fVect.append(0)

            #Numerical Data
            nnd = len([nd for nd in sentences[i] if nd.translate(None, '.,%').isdigit()])
            fVect.append(nnd/lengths[i])

            # Wordnet
            fVect.append(wordNetWeights[i])
            
            
            featureVectors.append(fVect)
            


    print featureVectors
