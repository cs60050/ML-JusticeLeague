from summa import summarizer
from summa.pagerank_weighted import pagerank_weighted_scipy as _pagerank
from summa.commons import build_graph as _build_graph
from summa.commons import remove_unreachable_nodes as _remove_unreachable_nodes
from math import log10 as _log10

#Overriding methods
def _get_similarity(s1, s2):
    common_word_count=0
    len_s1=0
    len_s2=0
    i=0
    while i<len(s1):
        if s1[i]!='0' and s2[i]!='0':
            common_word_count=common_word_count+1
        if s1[i]!='0':
            len_s1=len_s1+1
        if s2[i]!='0':
            len_s2=len_s2+1
        i=i+1
    if len_s1==0 or len_s2==0:
        return 0
    log_s1 = _log10(len_s1)
    log_s2 = _log10(len_s2)
    if log_s1+log_s2==0:
        return 0
    return common_word_count / (log_s1 + log_s2)

def summarize(sentences, ratio=0.2, words=None, language="english", split=False, scores=False):
    # Gets a list of processed sentences.
    # sentences = _clean_text_by_sentences(text, language)

    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    i=0
    while i<len(sentences):
        sentences[i]=''.join(str(x) for x in sentences[i])
        i=i+1

    graph = summarizer._build_graph(sentences)

    summarizer._set_graph_edge_weights(graph)

    # Remove all nodes with all edges weights equal to zero.
    _remove_unreachable_nodes(graph)

    # Ranks the tokens using the PageRank algorithm. Returns dict of sentence -> score
    pagerank_scores = _pagerank(graph)

    i=0
    scores_list=[]
    while i<len(sentences):
        if sentences[i] in pagerank_scores.keys():
            scores_list.append(pagerank_scores[sentences[i]])
        else:
            scores_list.append(0)
        i=i+1

    return scores_list

def modifiedSummarizer():
  summarizer._get_similarity = _get_similarity
  summarizer.summarize = summarize
  return summarizer
