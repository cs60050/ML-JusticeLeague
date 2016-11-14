#!/usr/bin/python

import sys
import csv
import random
import math

sys.path.insert(0, '../FeatureExtraction')
import nltk.data

reload(sys)  
sys.setdefaultencoding('utf8')

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 

import FeatureExtractor

# returns a list of lists
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	if(len(dataset[-1]) == 0):
		dataset = dataset[:-1] 			# trimming the last line of the csv file if it is empty

	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset

def loadFeatureData(filename):
	lines = csv.reader(open(filename, "rb"))
	lines_list = list(lines)
	if(len(lines_list[-1]) == 0):
		lines_list = lines_list[:-1] 			# trimming the last line of the file if it is empty

	feature_data = {}
	for line in lines_list:
		class_label = float(line[-1])
		feature_data[class_label] = []

		for feature_info in line[:-1]:
			feature_info = feature_info[1:-1]	# trimming the brackets at the two ends
			feature_metrics = feature_info.split(";")
			feature_metrics = [float(x) for x in feature_metrics]
			(feature_data[class_label]).append(tuple(feature_metrics))

	return feature_data
 
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
 
def classify(inputVectors, mode_num):
	if(mode_num == 1):
		filename = "../ModelCreation/mined_data_small.txt"				# consider that learned data is present in this file in the current directory
	else:
		filename = "../ModelCreation/mined_data_large.txt"
	summaries = loadFeatureData(filename)

	# use the learned model for predictions
	predictions = getPredictions(summaries,inputVectors)
	return predictions

def main():

	if(len(sys.argv) != 2):
		print "Please provide proper arguments... python giveSummary.py <path_to_the_input_doc> "
		return
	
	input_full_doc = sys.argv[1]

	try:
		f1 = open(input_full_doc,"r")
		#inputVectors = loadCsv(input_vector_file)
	except Exception,e:
		print "--- Could not access the the input file ---"
		# print e
		return
	full_doc = f1.read()
	full_doc_lines = tokenizer.tokenize(full_doc)
	full_doc_lines = filter(lambda a: a.strip() != ".", full_doc_lines)
	inputVectors = FeatureExtractor.extractFeatures(full_doc)
	if len(inputVectors) == len(full_doc_lines):
		predictions1 = classify(inputVectors, 1)
		predictions2 = classify(inputVectors, 2)
		f3 = open("output_largesumm.txt","w")
		cnt = 0
		for line in full_doc_lines:
			if predictions2[cnt] == 1:
				f3.write(line)
				f3.write("\n")
			cnt += 1

		f1.close()
		f3.close()

		f3 = open("output_smallsumm.txt","w")
		cnt = 0
		for line in full_doc_lines:
			if predictions1[cnt] == 1:
				f3.write(line)
				f3.write("\n")
			cnt += 1

		f1.close()
		f3.close()


	else:
		print "---Given vector file is inconsistent with the given full_doc---"
		f1.close()
	

main()