from math import log10 as _log10
from pagerank_weighted import pagerank_weighted_scipy as _pagerank
from commons import build_graph as _build_graph
from commons import remove_unreachable_nodes as _remove_unreachable_nodes


def _set_graph_edge_weights(graph):
    for sentence_1 in graph.nodes():
        for sentence_2 in graph.nodes():

            edge = (sentence_1, sentence_2)
            if sentence_1 != sentence_2 and not graph.has_edge(edge):
                similarity = _get_similarity(sentence_1, sentence_2)
                if similarity != 0:
                    graph.add_edge(edge, similarity)


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
    log_s1 = _log10(len_s1)
    log_s2 = _log10(len_s2)
    if log_s1+log_s2==0:
        return 0
    return common_word_count / (log_s1 + log_s2)


def _count_common_words(words_sentence_one, words_sentence_two):
    return len(set(words_sentence_one) & set(words_sentence_two))


def _format_results(extracted_sentences, split, score):
    if score:
        return [(sentence.text, sentence.score) for sentence in extracted_sentences]
    if split:
        return [sentence.text for sentence in extracted_sentences]
    return "\n".join([sentence.text for sentence in extracted_sentences])


def _add_scores_to_sentences(sentences, scores):
    for sentence in sentences:
        # Adds the score to the object if it has one.
        if sentence in scores:
            sentence.score = scores[sentence]
        else:
            sentence.score = 0


def _get_sentences_with_word_count(sentences, words):
    """ Given a list of sentences, returns a list of sentences with a
    total word count similar to the word count provided.
    """
    word_count = 0
    selected_sentences = []
    # Loops until the word count is reached.
    for sentence in sentences:
        words_in_sentence = len(sentence.text.split())

        # Checks if the inclusion of the sentence gives a better approximation
        # to the word parameter.
        if abs(words - word_count - words_in_sentence) > abs(words - word_count):
            return selected_sentences

        selected_sentences.append(sentence)
        word_count += words_in_sentence

    return selected_sentences


def _extract_most_important_sentences(sentences, ratio, words):
    sentences.sort(key=lambda s: s.score, reverse=True)

    # If no "words" option is selected, the number of sentences is
    # reduced by the provided ratio.
    if words is None:
        length = len(sentences) * ratio
        return sentences[:int(length)]

    # Else, the ratio is ignored.
    else:
        return _get_sentences_with_word_count(sentences, words)


def summarize(sentences, ratio=0.2, words=None, language="english", split=False, scores=False):
    # Gets a list of processed sentences.
    # sentences = _clean_text_by_sentences(text, language)

    # Creates the graph and calculates the similarity coefficient for every pair of nodes.
    i=0
    while i<len(sentences):
        sentences[i]=''.join(str(x) for x in sentences[i])
        i=i+1

    graph = _build_graph(sentences)

    _set_graph_edge_weights(graph)

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


def get_graph(text, language="english"):
    sentences = _clean_text_by_sentences(text, language)

    graph = _build_graph([sentence.token for sentence in sentences])
    _set_graph_edge_weights(graph)

    return graph
