from math import log10 as _log10

def get_similarity(str1, str2):

	n1 = len(str1)
	n2 = len(str2)
	
	min = n2
	if n1 < n2:
		min = n1

	i = 0
	match = 0
	l1 = 0
	l2 = 0
	while i < min:
		if str1[i]=='1' and str2[i]=='1':
			match = match+1
		if str1[i]=='1':
			l1 = l1+1
		if str2[i]=='1':
			l2 = l2+1
		i = i+1

	if l1==0 or l2==0:
		return 0

	if _log10(l1)+_log10(l2)==0:
		return 0

	return match / (_log10(l1)+_log10(l2))


def page_rank(wordList):

	n = len(wordList)
	adjMat = [[0 for x in range(n)] for y in range(n)]

	for i in range(n):
		for j in range(n):
			adjMat[i][j] = get_similarity(wordList[i], wordList[j])

	rank = [0 for x in range(n)]

	for i in range(n):
		sum = 0
		for j in range(n):
			if i != j:
				sum = sum + adjMat[i][j]
		rank[i] = sum

	return rank
	#for i in 

