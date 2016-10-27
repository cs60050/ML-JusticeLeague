#!/usr/bin/python

import csv
import random
import math

# returns a list of lists
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def separateByClass(dataset):
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if (vector[-1] not in separated):
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated
 
def mean(numbers):
	return sum(numbers)/float(len(numbers))
 
def stdev(numbers):
	avg = mean(numbers)
	variance = sum([pow(x-avg,2) for x in numbers])/float(len(numbers))
	return math.sqrt(variance)
 
def summarize(dataset):
	summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summaries[-1]
	return summaries
 
def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summaries = {}
	for classValue, instances in separated.iteritems():
		summaries[classValue] = summarize(instances)
	return summaries
 
def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
 
def calculateClassProbabilities(summaries, inputVector):
	probabilities = {}
	for classValue, classSummaries in summaries.iteritems():
		probabilities[classValue] = 1
		for i in range(len(classSummaries)):
			mean, stdev = classSummaries[i]
			x = inputVector[i]
			probabilities[classValue] *= calculateProbability(x, mean, stdev)
	return probabilities
			
def predict(summaries, inputVector):
	probabilities = calculateClassProbabilities(summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.iteritems():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel
 
def getPredictions(summaries, testSet):
	predictions = []
	for i in range(len(testSet)):
		result = predict(summaries, testSet[i])
		predictions.append(result)
	return predictions
 
def getAccuracy(testSet, predictions):
	correct = 0
	for i in range(len(testSet)):
		if testSet[i][-1] == predictions[i]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
 
def classify():

	filename = 'train_set.csv'
	trainingSet = loadCsv(filename)

	filename = 'test_set.csv'
	testSet = loadCsv(filename)

	# prepare model
	summaries = summarizeByClass(trainingSet)

	# test model
	predictions = getPredictions(summaries, testSet)
	return predictions

def main():

	num_train_docs = 1
	f3 = open("train_set.csv","w")
	f4 = open("train_len.csv","w")
	list2 =[]
	list3= [3,4,10,20,50,51,89,111,113,120]
	cnt4 =0
	for i in range(1,121):

		if not i in list3:
			str1 = "./training/FullDocs/"+str(i) + "_fulldoc.txt"
			str2 = "./training/SmallSumms/"+str(i) + "_smallsumm.txt"
			str3 = str(i) + "_vec.csv"

			f1 = open(str1,"r")
			f2 = open(str2,"r")
			sentenceVectors = loadCsv(str3)
			
			list1 = f2.read().splitlines()

			full_doc_lines = f1.read().splitlines()
			list2[:] = []
			for line in full_doc_lines:
				if line in list1:
					list2.append(1)
				else:
					list2.append(0)
			f4.write(str(i))
			f4.write("\n")
			cnt = long(0)
			for sentVec in sentenceVectors:

				for featureVal in sentVec:
					f3.write(str(featureVal))
					f3.write(",")

				sentenceLabel = list2[cnt]
				f3.write(str(sentenceLabel))
				f3.write("\n")
				cnt += 1

			f1.close()
			f2.close()

	f3.close()
	f4.close()

	f3 = open("test_set.csv","w")
	f4 = open("test_len.csv","w")
	list4 = [123,128,158,179]
	for i in range(121,213):
		if not i in list4:
			str1 = "./test/FullDocs/"+str(i) + "_fulldoc.txt"
			str2 = "./test/SmallSumms/"+str(i) + "_smallsumm.txt"
			str3 = str(i) + "_vec.csv"

			f1 = open(str1,"r")
			f2 = open(str2,"r")
			sentenceVectors = loadCsv(str3)
			
			list1 = f2.read().splitlines()

			full_doc_lines = f1.read().splitlines()
			list2[:] = []
			for line in full_doc_lines:
				if line in list1:
					list2.append(1)
				else:
					list2.append(0)
			f4.write(str(i))
			f4.write("\n")
			cnt = long(0)
			for sentVec in sentenceVectors:

				for featureVal in sentVec:
					f3.write(str(featureVal))
					f3.write(",")

				sentenceLabel = list2[cnt]
				f3.write(str(sentenceLabel))
				f3.write("\n")
				cnt += 1

			f1.close()
			f2.close()

	f3.close()
	f4.close()

	predictions = classify()

	filename = 'test_set.csv'
	testSet = loadCsv(filename)

	accuracy = getAccuracy(testSet,predictions)
	print accuracy
	# f1 = open("input_fulldoc.txt","r")
	# f2 = open("output_smallsumm.txt","w")

	# cnt = 0
	# for line in f1:
	# 	if predictions[cnt] == 1:
	# 		f2.write(line)
	# 	cnt += 1

	# f1.close()
	# f2.close()

main()